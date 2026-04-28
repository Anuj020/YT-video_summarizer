# 🚀 YouTube Video Summarizer using CrewAI (Multi-Agent System)

An AI-powered multi-agent system that extracts insights from YouTube videos and converts them into structured blog content using CrewAI, LangChain, and LLMs.

## 🧠 Project Overview

This project builds a multi-agent system where different AI agents collaborate to research YouTube videos and generate structured blog content.

The system:
- Takes a topic as input
- Finds relevant YouTube content
- Extracts insights using tools
- Generates a clean blog-style summary

## ⚙️ Tech Stack

- CrewAI
- LangChain
- OpenAI / Gemini LLM
- Python
- Serper API
- YouTube tools
- dotenv

## 🏗️ Architecture

User Input (Topic) → Research Agent → Data Extraction → Writer Agent → Final Blog Output (.md)

## 🤖 Agents

Blog Researcher Agent:
- Searches YouTube content
- Extracts key insights
- Passes structured data forward

Blog Writer Agent:
- Converts research into readable blog format
- Simplifies technical content
- Generates final markdown output

## 🧰 Tools Used

- SerperDevTool (web search)
- YoutubeChannelSearchTool (YouTube extraction)

## 📁 Project Structure
```bash
AgenticAI/
│── crewAI.py
│── agents.py
│── tasks.py
│── tools.py
│── new-blog-post.md
│── .env
```


## 🚀 Setup Instructions

###  1️⃣ Clone Repository
```bash
    git clone https://github.com/Anuj020/YT-video_summarizer.git
    cd YT-video_summarizer
```

  ###  2️⃣ Create Virtual Environment
```bash
    python -m venv venv
    source venv/bin/activate
```
   ### 3️⃣ Install Requirements
```bash
    pip install -r requirements.txt
```

 ### 4️⃣ Add Environment Variables

```ini
        OPENAI_API_KEY=your_key
```



Run project:
python crewAI.py

## 📌 Output

Generated blog is saved in:
new-blog-post.md

## 🧩 Key Learnings

- Multi-agent system design using CrewAI
- Tool-augmented LLM pipelines
- Real-world AI workflow orchestration
- Debugging API + tool + loader issues
- Building modular AI systems



## 👨‍💻 Author

Anuj Patel  
GitHub: https://github.com/Anuj020

## ⭐ Support

If you like this project, give it a star on GitHub
