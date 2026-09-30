# 🎓 RAG-Based Teaching Assistant 

A **Retrieval-Augmented Generation (RAG)** based AI teaching assistant trained on the first 18 videos of the **Sigma Web Development Course**.  
This web app answers questions related to the course — such as *“When is CSS taught in this course?”* — and provides both the **time and context** of the topic along with a **brief explanation**.

---

## 🚀 Overview

This project demonstrates how RAG can be used to build a **domain-specific AI tutor**.  
The assistant processes course videos, converts them into embeddings, and uses **Llama 3.2** as the reasoning engine to answer user questions with precise context from the training material.

---
🔗 **Web App Screenshots:**
![demoIMG](https://github.com/arnavkakkar/RAG-based-AI-assistant/blob/8fbbd7db86e7197635f6353ccb317eff80b4dfbd/img/demo%20img.png)

## ⚙️ How It Works

1. **Video Processing:**  
   Each lecture video is converted to `.mp3` using **FFmpeg**.

2. **Transcription:**  
   Audio files are transcribed into text using **OpenAI Whisper** and stored as `.json` files.

3. **Embedding Generation:**  
   The JSON transcripts are converted into vector embeddings using the **bge-m3** embedding model.

4. **Knowledge Base Creation:**  
   The embeddings are stored as a **DataFrame** and serialized using `joblib` for fast retrieval.

5. **Question Answering:**  
   - User queries are converted into embeddings using **bge-m3**.  
   - The system finds the most relevant video chunks using **FAISS** vector similarity search.  
   - **LangChain's PromptTemplate** combines the retrieved subtitle context and user query into a structured prompt.  
   - The prompt is then sent to **Llama 3.2** to generate a detailed answer.

6. **Web App Interface:**  
   A **Flask** web app provides a simple front-end where users can ask questions and view responses.

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Python, Flask |
| AI Model | Llama 3.2 |
| Embeddings | bge-m3 |
| Vector Retrieval | FAISS |
| Prompt Templating | LangChain (PromptTemplate) |
| Speech-to-Text | OpenAI Whisper |
| Video Processing | FFmpeg |
| Storage | JSON, Joblib |

---

## 💻 Setup and Usage

### Step 0 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 1 — Collect Your Videos
Move all your course videos into the `Videos/` folder.

### Step 2 — Convert to MP3

Convert all the video files to mp3 by ruunning video_to_mp3.py

### Step 3 — Transcribe Audio to JSON

Convert all the mp3 files to json by ruunning mp3_to_json.py

### Step 4 — Generate Embeddings

python json_preprocessing.py
This will convert the JSON transcripts into embeddings and save them as a `.joblib` file.

### Step 5 — Start the Web App

python app.py

Then open your browser and visit:
```
http://localhost:5000
```

Ask any question related to your course — the assistant will retrieve relevant content and answer using Llama 3.2.

---

## 🧩 Example Query

> **User:** When is CSS taught in this course?  
> **Assistant:** Hi there! So you're curious about when CSS is taught in our Sigma web development course? CSS is actually introduced in Video 14, titled "Introduction to CSS". If you want to watch that video and learn more about CSS. In this video, we cover some basics of CSS, including its importance in web development and how to use it to style your website. We also talk about CSS selectors, which are a crucial part of understanding CSS. If you're interested in learning more about CSS, I recommend checking out Video 14, where you'll learn about the basics of CSS and how to apply them to your own projects. Would you like some more information on CSS or help finding the video?

---




##  Author

**Arnav Kakkar**  

