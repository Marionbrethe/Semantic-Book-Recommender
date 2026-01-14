# Semantic-Book-Recommender

A personalized book recommendation engine that combines LLM reasoning (GPT-4o) with semantic search (Embeddings) to discover books that match your specific reading taste.

Unlike standard collaborative filtering (which suggests "people who bought X also bought Y"), this project builds a mathematical representation of your personal "Taste Vector" based on book descriptions and your specific ratings, then finds and explains new books that align with that vector.

🚀 How It Works
The system operates as a six-step pipeline. It moves from raw Goodreads data to a final, curated list of recommendations with explanations.

The Pipeline
Ingest & Clean: Loads your raw ratings export (e.g., from Goodreads), filters for books you've actually rated, and normalizes the data.
Enrich Data: Queries the Open Library API to fetch descriptions, subjects, and publication years for your rated books to add context beyond just the title.
Build Taste Vector: Converts book descriptions into vector embeddings using text-embedding-3-small. Computes a User Taste Vector by taking a weighted average of your book embeddings (weighted by your rating, centered so low ratings don't negatively impact the vector).
Generate Candidates: Uses an LLM (gpt-4o-mini) to brainstorm a raw list of potential books based on a textual summary of your favorites, then validates they are real books via Open Library.
Semantic Ranking: Embeds the candidate books and ranks them by Cosine Similarity against your Taste Vector. This finds books that mathematically feel like your favorites.
LLM Reranking & Explaining: The top candidates are sent back to the LLM to be re-ranked based on nuance, tone, and diversity. The LLM writes a final "Why this matches" explanation for the user.

🛠️ Tech Stack
Python 3.x
OpenAI API: Used for Embeddings (text-embedding-3-small) and Generation (gpt-4o-mini).
Open Library API: Free API used for metadata validation and book descriptions.
Pandas & NumPy: Data manipulation and vector math.
Scikit-Learn: Used for Cosine Similarity calculations.

Substack article - WIP 
