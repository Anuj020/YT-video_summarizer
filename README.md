# 🚀 YouTube Video Summarizer using CrewAI (Multi-Agent System)

An AI-powered multi-agent system that extracts insights from YouTube videos and converts them into structured blog content using CrewAI, LangChain, and LLMs.

---

## 🧠 Project Overview

This project demonstrates a **multi-agent AI workflow** where agents collaborate to:

- 🔍 Research YouTube video content based on a topic  
- 🎥 Extract relevant insights using search tools  
- ✍️ Generate structured blog-style summaries  
- 🤖 Work together using CrewAI orchestration  

Instead of a single LLM call, this system simulates a real-world AI team with specialized roles.

---

## ⚙️ Tech Stack

- CrewAI (Multi-agent orchestration)
- LangChain
- OpenAI
- YouTube
- Python
- RAG-style tool-based memory

---

## 🏗️ Architecture

User Input (Topic)
        ↓
Research Agent (YouTube/Search Tools)
        ↓
Processed Insights
        ↓
Writer Agent
        ↓
Final Blog Output (.md file)

---

## 🤖 Agents

### 🔍 Blog Researcher Agent
- Searches and gathers relevant YouTube video content  
- Extracts useful insights  
- Passes structured information to writer agent  

### ✍️ Blog Writer Agent
- Converts research into structured blog content  
- Simplifies technical concepts  
- Produces final markdown output  

---

## 🧰 Tools Used

- SerperDevTool → Web search  
- YoutubeChannelSearchTool → YouTube content extraction  

---

## 📁 Project Structure

AgenticAI/
│── crewAI.py          # Main execution file  
│── agents.py          # Agent definitions  
│── tasks.py           # Task workflow  
│── tools.py           # Tools setup  
│── new-blog-post.md   # Output file  
│── .env               # API keys (not committed)  

---

## 🚀 Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/Anuj020/YT-video_summarizer.git
cd YT-video_summarizer
