# 🚀 RAG-Based AI Assistant

An end-to-end Retrieval-Augmented Generation (RAG) AI assistant that processes YouTube videos, converts them into structured knowledge, and answers user queries using semantic similarity search and Large Language Models (LLMs).

This project builds a complete pipeline from raw video content → transcript processing → embeddings → intelligent question answering.

---

## 📌 Project Overview

Traditional LLMs generate responses based only on trained knowledge, which may lead to hallucinations.

This system solves that by:

1. Extracting audio from videos
2. Generating transcript JSON files
3. Cleaning and merging text chunks
4. Generating embeddings using Sentence Transformers
5. Storing embeddings locally using `joblib`
6. Retrieving top-K relevant chunks using cosine similarity
7. Passing context to an LLM for grounded answer generation

---

## 🧠 Architecture Flow

YouTube Video  
↓  
Audio Extraction (`video_to_mp3.py`)  
↓  
Speech-to-Text → JSON (`mp3_to_json.py`)  
↓  
Preprocessing & Cleaning (`preprocess_json.py`)  
↓  
Chunk Merging (`merge_chunks.py`)  
↓  
Embedding Generation  
↓  
Store Embeddings (`embeddings.joblib`)  
↓  
User Query  
↓  
Query Embedding  
↓  
Cosine Similarity Search  
↓  
Retrieve Top-K Chunks  
↓  
LLM Generates Final Answer  

---

## 🛠️ Tech Stack

- Python  
- Sentence Transformers (Embeddings)  
- OpenAI API / LLM API  
- NumPy  
- Pandas  
- Scikit-learn (Cosine Similarity)  
- Joblib (Embedding Storage)  
- JSON Processing  

---

## 📂 Project Structure
rag-ai-assistant/
│
├── audios/ # Extracted audio files (ignored in repo)
├── videos/ # Source videos (ignored in repo)
├── jsons/ # Raw transcript JSON files
├── newjsons/ # Cleaned JSON files
├── unused/ # Temporary files
│
├── video_to_mp3.py # Extract audio from video
├── mp3_to_json.py # Convert audio to transcript JSON
├── preprocess_json.py # Clean transcript data
├── merge_chunks.py # Merge text into semantic chunks
├── process_incoming.py # Automates full pipeline
│
├── embeddings.joblib # Stored document embeddings
├── output.json # Final processed structured text
├── prompt.txt # Prompt template for LLM
├── response.txt # Generated response output
│
└── README.md


---

## ⚙️ Installation

### 1️⃣ Clone the Repository

### 2️⃣ Create Virtual Environment (Mac)

### 3️⃣ Install Dependencies

### 4️⃣ Add API Key

Create a `.env` file:

---

## ▶️ How to Use

### Step 1: Provide Video Files

Place videos inside:

(These files are ignored in the public repository due to copyright restrictions.)

---

### Step 2: Run Full Processing Pipeline

This will:
- Extract audio
- Generate transcripts
- Clean and merge chunks
- Generate embeddings
- Save embeddings to `embeddings.joblib`

---

### Step 3: Ask Questions

Run your query interface:

System will:
- Convert query into embedding
- Load stored embeddings
- Compute cosine similarity
- Retrieve most relevant chunks
- Generate grounded answer using LLM

---

## 🔎 Retrieval Logic

- Query embedding generated at runtime
- Stored embeddings loaded from `joblib`
- Cosine similarity computed
- Top-K relevant chunks selected
- Context passed into LLM prompt template
- LLM generates final response

---

## 📊 Key Features

✅ End-to-end multimodal pipeline  
✅ Automatic video → transcript processing  
✅ Custom chunking strategy  
✅ Local embedding storage (no external vector DB)  
✅ Fast semantic similarity retrieval  
✅ Modular architecture  
✅ Reduced hallucination using RAG  

---

## 📌 Note on Media Files

Due to copyright restrictions, source video and audio files are not included in this repository.  
Users can provide their own YouTube videos or media files for processing.

---

## 📈 Future Improvements

- Hybrid Search (BM25 + Vector Search)  
- Conversational Memory  
- Real-time streaming transcription  
- Web-based UI  
- Docker deployment  
- Retrieval evaluation metrics (Recall@K, MRR)  

---

## 👨‍💻 Author

Akshat Singh  
B.Tech Student | AI/ML Enthusiast  
Open to AI/ML Internship Opportunities  

---

## ⭐ Why This Project Matters

This project demonstrates:

- Real-world implementation of Retrieval-Augmented Generation  
- Multimodal AI system design  
- Embedding generation and optimization  
- Cosine similarity-based retrieval  
- Prompt engineering  
- End-to-end AI pipeline development  

If you found this project useful, consider giving it a ⭐