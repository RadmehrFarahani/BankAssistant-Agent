# 🏦 Bank Assistant

An AI-powered banking assistant built with **Python, Streamlit, LangChain, and Ollama**.

The project uses **Few-Shot Prompting** to provide contextual banking responses based on predefined examples and the selected banking service.

## ✨ Features

* 🤖 AI-powered banking assistant
* 🧠 Few-Shot Prompting
* 🎯 Dynamic example selection with `LengthBasedExampleSelector`
* 🦙 Local LLM with Ollama & Llama 3.2
* 🏦 Multiple banking service categories
* ⚡ Streaming responses with Streamlit

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Ollama
* Llama 3.2

## 🧠 How It Works

```text
User Question
     ↓
Select Banking Service
     ↓
Few-Shot Examples
     ↓
Prompt Template
     ↓
Llama 3.2 (Ollama)
     ↓
AI Response
```

The application uses `LengthBasedExampleSelector` to select suitable examples and `FewShotPromptTemplate` to build the final prompt before sending it to the LLM.

## 🚀 Run Locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Install and run Ollama, then download the model:

```bash
ollama pull llama3.2
```

Start the application:

```bash
streamlit run app.py
```

## 📚 Concepts

This project demonstrates:

* LangChain Prompt Templates
* Few-Shot Prompting
* Example Selection
* Local LLMs
* Streamlit
* Ollama

## 👨‍💻 Author

**Radmehr Farahani**

Backend Developer | AI & LLM Enthusiast

📧 [radmehrfarahani82@gmail.com](mailto:radmehrfarahani82@gmail.com)
