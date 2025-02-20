# **📚 AI-Powered Book Recommendation**  

### **🔗 Live Demo:** [View on Hugging Face Spaces](https://huggingface.co/spaces/jishnu23/book-reccommendation-system)

---

## **📖 About The Project**
This project builds an **AI-powered book recommendation system** using NLP techniques. The system includes:  
- **Vector Search**: Semantic search for books using **LangChain**, **HuggingFace Embeddings** (`BAAI/bge-small-en`), and **Chroma**.
- **Text Classification**: Predicts missing book categories using a fine-tuned **DistilBERT** (`distilbert-base-uncased`) model with **87% accuracy**.  
- **Sentiment Analysis**: Uses **DistilRoBERTa** (`j-hartmann/emotion-english-distilroberta-base`) to assign **emotion scores** (joy, sadness, anger, fear, surprise, neutral).  
- **Gradio Dashboard**: Allows users to search for books by title, filter by category, and sort by emotions.  

**🔍 Key Features:**
✔️ Intelligent **semantic search** for books  
✔️ **Missing category classification** using DistilBERT  
✔️ **Emotion-based filtering** (joy, sadness, anger, etc.)  
✔️ Interactive **Gradio web app** for easy book discovery  

<p align="right">(<a href="#top">⬆ Back to top</a>)</p>

---

## **⚙️ Built With**
- **Python** (3.11.4)
- **LangChain** (`TextLoader`, `CharacterTextSplitter`)
- **Hugging Face Transformers**
  - `BAAI/bge-small-en` (Embeddings for semantic search)
  - `distilbert-base-uncased` (Book category classification)
  - `j-hartmann/emotion-english-distilroberta-base` (Sentiment analysis)
- **Chroma** (Vector storage)
- **Gradio** (Web interface)

<p align="right">(<a href="#top">⬆ Back to top</a>)</p>

---

## **🚀 Getting Started**
### **🔧 Prerequisites**
Ensure you have the following installed:
- Python 3.11.4+
- `pip` and `virtualenv`

### **📦 Installation**
1️⃣ **Clone the repository**  
```sh
git clone https://github.com/jishnu3000/llm-book-recommender.git
cd llm-book-recommender
```
2️⃣ **Create a virtual environment and install dependencies**  
```sh
python -m venv venv
source venv/bin/activate   # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```
3️⃣ **Run the Gradio app**  
```sh
python app.py
```
4️⃣ **Open in browser**  
Gradio will provide a **local URL** to access the app.

<p align="right">(<a href="#top">⬆ Back to top</a>)</p>

---

## **🛠️ Usage**
### **🔎 Searching for Books**
- Enter a **book title** or keyword.
- The system performs **semantic search** and retrieves the most relevant books.

### **📌 Filtering by Category**
- Missing categories are predicted using **DistilBERT**.
- Users can filter books by **category**.

### **🎭 Emotion-Based Sorting**
- Books are analyzed for **sentiment**.
- Users can sort books based on **emotion scores** (joy, sadness, anger, etc.).

### **🌐 Live Demo**
Try it out on **Hugging Face Spaces**: [View Demo](https://huggingface.co/spaces/jishnu23/book-reccommendation-system)

<p align="right">(<a href="#top">⬆ Back to top</a>)</p>

---

## **📜 License**
Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

<p align="right">(<a href="#top">⬆ Back to top</a>)</p>

---

## **🌟 Acknowledgments**
- [Hugging Face](https://huggingface.co/) for transformers & embeddings
- [LangChain](https://python.langchain.com/) for vector search
- [Gradio](https://gradio.app/) for building an interactive UI

<p align="right">(<a href="#top">⬆ Back to top</a>)</p>

---

🚀 **Ready to explore AI-powered book search?** [Try it now!](https://huggingface.co/spaces/jishnu23/book-reccommendation-system)