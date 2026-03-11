# 🚀 RAG-Based AI Assistant

An end-to-end **Retrieval-Augmented Generation (RAG)** AI assistant that processes YouTube videos and playlists, converts them into structured knowledge, and answers user queries using semantic similarity search and Large Language Models (LLMs).

This project builds a complete pipeline from **raw video content → transcript processing → embeddings → intelligent question answering**.

---

# 📌 Project Overview

Traditional LLMs generate responses based only on their trained knowledge, which may lead to hallucinations.

This system solves that by retrieving **relevant information directly from video transcripts** before generating answers.

The system supports two ingestion strategies:

1. **Caption Extraction (Fast Method)** – Directly fetches captions from YouTube.
2. **Audio Transcription (Fallback Method)** – Converts video audio into transcripts when captions are unavailable.

---

# 🧠 Architecture Flow

## Caption-Based Pipeline (Fast Path)

YouTube URL / Playlist
↓
Caption Extraction (`youtube_caption_to_json.py`)
↓
Transcript JSON Generation
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

## Audio Transcription Pipeline (Fallback)

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

# 🛠️ Tech Stack

* Python
* Sentence Transformers (Embeddings)
* Ollama (Local LLM)
* NumPy
* Pandas
* Scikit-learn (Cosine Similarity)
* Joblib (Embedding Storage)
* YouTube Transcript API
* PyTube

---

# 📂 Project Structure

```
rag-ai-assistant/
│
├── audios/                 # Extracted audio files (ignored in repo)
├── videos/                 # Source videos (ignored in repo)
├── jsons/                  # Raw transcript JSON files
├── newjsons/               # Cleaned JSON files
├── yt_jsons/               # Captions extracted from YouTube
├── unused/                 # Temporary files
│
├── youtube_caption_to_json.py   # Extract captions from YouTube videos/playlists
├── video_to_mp3.py              # Extract audio from video
├── mp3_to_json.py               # Convert audio to transcript JSON
├── preprocess_json.py           # Clean transcript data
├── merge_chunks.py              # Merge text into semantic chunks
├── process_incoming.py          # Automates full pipeline
│
├── embeddings.joblib       # Stored document embeddings
├── output.json             # Final processed structured text
├── prompt.txt              # Prompt template for LLM
├── response.txt            # Generated response output
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/rag-ai-assistant.git
cd rag-ai-assistant
```

---

## 2️⃣ Create Virtual Environment (Mac/Linux)

```
python -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

# ▶️ How to Use

## Option 1: Process YouTube URL or Playlist (Fast Method)

Run:

```
python youtube_caption_to_json.py "YOUTUBE_URL"
```

This will:

* Extract captions
* Convert them to structured JSON
* Save them in `yt_jsons/captions.json`

Example:

```
python youtube_caption_to_json.py "https://youtu.be/VIDEO_ID"
```

or

```
python youtube_caption_to_json.py "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

---

## Option 2: Process Local Videos (Fallback Method)

Place videos inside:

```
videos/
```

Then run the full pipeline:

```
python process_incoming.py
```

This will:

* Extract audio
* Generate transcripts
* Clean and merge chunks
* Generate embeddings
* Save embeddings to `embeddings.joblib`

---

# ❓ Ask Questions

Run your query interface:

```
python process_incoming.py
```

The system will:

1. Convert query into embedding
2. Load stored embeddings
3. Compute cosine similarity
4. Retrieve most relevant chunks
5. Generate grounded answer using Ollama LLM

---

# 🔎 Retrieval Logic

* Query embedding generated at runtime
* Stored embeddings loaded from `joblib`
* Cosine similarity computed
* Top-K relevant chunks selected
* Context passed into LLM prompt template
* LLM generates final response

---

# 📊 Key Features

✅ End-to-end RAG pipeline
✅ Supports **YouTube videos and playlists**
✅ Caption-based ingestion (fast processing)
✅ Audio transcription fallback
✅ Custom chunking strategy
✅ Local embedding storage (no external vector DB)
✅ Fast semantic similarity retrieval
✅ Modular architecture
✅ Reduced hallucination using RAG

---

# 📌 Note on Media Files

Due to copyright restrictions, source video and audio files are not included in this repository.

Users can provide their own YouTube URLs or media files for processing.

---

# 📈 Future Improvements

* Timestamp-based answers from videos
* Hybrid Search (BM25 + Vector Search)
* Conversational Memory
* Web-based UI
* Vector database integration (FAISS / ChromaDB)
* Docker deployment
* Retrieval evaluation metrics (Recall@K, MRR)

---

# 👨‍💻 Author

Akshat Singh
B.Tech Student | AI/ML Enthusiast

Open to **AI / ML Internship Opportunities**

---

# ⭐ Why This Project Matters

This project demonstrates:

* Real-world implementation of **Retrieval-Augmented Generation**
* **Multimodal AI system design**
* Embedding generation and optimization
* Cosine similarity-based retrieval
* Prompt engineering
* End-to-end AI pipeline development

If you found this project useful, consider giving it a ⭐
