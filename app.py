import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os

from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma

import gradio as gr

load_dotenv()

books = pd.read_csv('books_with_emotions.csv')
books["large_thumbnail"] = books["thumbnail"] + "&fife=w800"
books["large_thumbnail"] = np.where(
    books["thumbnail"].isna(),
    "./images/cover-not-found.jpg",
    books["large_thumbnail"]
)

DB_DIR = "chroma_db"

raw_documents = TextLoader("tagged_description.txt", encoding="utf-8").load()
text_splitter = CharacterTextSplitter(separator='\n', chunk_size=0, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en")
db_books = Chroma.from_documents(documents, embeddings, persist_directory=DB_DIR)

def retrieve_semantic_recommendations(
    query: str,
    category: str = None,
    tone: str = None,
    initial_top_k: int = 50,
    final_top_k: int = 16
) -> pd.DataFrame:
  recs = db_books.similarity_search(query, k=initial_top_k)
  books_list = [int(rec.page_content.strip('"').split()[0]) for rec in recs]
  books_recs = books[books["isbn13"].isin(books_list)].head(final_top_k)

  if category != 'All':
    books_recs = books_recs[books_recs["simple_categories"] == category][:final_top_k]
  else:
    books_recs = books_recs.head(final_top_k)

  if tone == "Happy":
    books_recs.sort_values(by="joy", ascending=False, inplace=True)
  elif tone == "Surprising":
    books_recs.sort_values(by="surprise", ascending=False, inplace=True)
  elif tone == "Angry":
    books_recs.sort_values(by="anger", ascending=False, inplace=True)
  elif tone == "Suspensful":
    books_recs.sort_values(by="fear", ascending=False, inplace=True)
  elif tone == "Sad":
    books_recs.sort_values(by="sadness", ascending=False, inplace=True)
  elif tone == "Love":
    books_recs.sort_values(by="love", ascending=False, inplace=True)

  return books_recs


def recommend_books(
    query: str,
    category: str,
    tone: str
):
  recommendations = retrieve_semantic_recommendations(query, category, tone)
  results = []

  for _, row in recommendations.iterrows():
    description = row["description"]
    truncated_desc_split = description.split()
    truncated_desc = " ".join(truncated_desc_split[:30]) + "..."

    authors_split = row["authors"].split(";")
    if len(authors_split) == 2:
      authors_str = f"{authors_split[0]} and {authors_split[1]}"
    elif len(authors_split) > 2:
      authors_str = f"{', '.join(authors_split[:-1])} and {authors_split[-1]}"
    else:
      authors_str = row["authors"]

    caption = f"{row['title']} by {authors_str}: {truncated_desc}"
    results.append((row["large_thumbnail"], caption))

  return results


categories = ['All'] + sorted(books["simple_categories"].unique())
tones = ['All'] + ['Happy', 'Surprising', 'Angry', 'Suspensful', 'Sad']

custom_css = """
h1 {
    text-align: center;
    color: #333;
    font-size: 2.5em;
}
body {
    background-color: #f7f7f7;
    font-family: 'Arial', sans-serif;
}
.gr-button {
    background-color: #0056b3;
    color: white;
    font-weight: bold;
}
.gr-button:hover {
    background-color: #003d82;
}
.gr-textbox {
    border-radius: 10px;
}
"""

# Gradio App with a Professional Theme
with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as dashboard:
  gr.Markdown("# Semantic Book Recommendation System")

  with gr.Row():
    user_query = gr.Textbox(label="Please enter a description of a book:",placeholder="e.g. a story about forgiveness")
    category_dropdown = gr.Dropdown(choices=categories, label="Select a category:", value="All")
    tone_dropdown = gr.Dropdown(choices=tones, label="Select a tone:", value="All")
    submit_button = gr.Button("Find Recommendations")

  gr.Markdown("## Recommendations")

  default_covers = [
      ("./images/cover-not-found.jpg", "No recommendation yet! Enter a query."),
  ]

  output = gr.Gallery(label="Recommended Books", columns=8, rows=2, value=default_covers)

  submit_button.click(recommend_books, inputs=[user_query, category_dropdown, tone_dropdown], outputs=output)

if __name__ == "__main__":
  dashboard.launch()
