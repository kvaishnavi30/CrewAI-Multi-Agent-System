# 🤖 CrewAI Multi-Agent Research & Writing System

This project demonstrates a simple multi-agent AI workflow using CrewAI and Ollama. It consists of two AI agents: a Research Agent that gathers information on a given topic and a Technical Writer Agent that summarizes the research into a structured report.

## 🚀 Features

- Multi-agent collaboration using CrewAI
- Research Agent for information gathering
- Technical Writer Agent for content summarization
- Sequential task execution
- Local LLM integration with Ollama
- Generates concise Markdown reports

## 🛠️ Technologies Used

- Python
- CrewAI
- Ollama
- Gemma LLM

## 📁 Project Structure

```
CrewAI-Multi-Agent-System/
│── app.py
│── requirements.txt
│── README.md
```

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/CrewAI-Multi-Agent-System.git
```

2. Navigate to the project folder:

```bash
cd CrewAI-Multi-Agent-System
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Make sure Ollama is installed and the Gemma model is available:

```bash
ollama pull gemma
```

## ▶️ Run the Project

```bash
python app.py
```

## 📌 Workflow

1. The **Research Agent** collects information on the given topic.
2. The **Technical Writer Agent** summarizes the research.
3. The Crew executes tasks sequentially and displays the final output.

## 📦 Requirements

- crewai
- ollama

## 👩‍💻 Author

K. Vaishnavi

## 📄 License

This project is created for learning and educational purposes.
