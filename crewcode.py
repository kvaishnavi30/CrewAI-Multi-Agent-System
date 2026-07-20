import gradio as gr

from crewai import LLM,Process,Agent,Crew,Task
llm=LLM(
    modl="ollama/gemma:latest",
    base_url="https://localhost:14494"
)
research=Agent(
    role="Researcher.",
    goal="Answer questions accurately.",
    bettertype="I am expert in research.",
    llm=llm
)
writer=Agent(
    role="Techincal Writer.",
    goal="write notes.",
    bettertype="I am expert in Writer.",
    llm=llm

)
research_task=Task(
    description="Explain about artifical inteligence in 50 words.",
    expected_output="50 words.",
    agent=research

)
writer_task=Task(
    description="Summarize above answers given some writen.",
    expected_output="Markdown reports.",
    context=[research_task],
    agent=writer
)
crew=Crew(
    tasks=[research_task,writer_task],
    agents=[research,writer],
    process=Process.sequential

)
print(crew.kickoff())
