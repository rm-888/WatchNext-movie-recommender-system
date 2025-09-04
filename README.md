# 🔎 WatchNext: Movie Recommender

A **movie recommendation system** built using Python and Streamlit. This app suggests movies similar to your selection using a combination of **genres, keywords, cast, crew, and tags** from the TMDB 5000 Movies dataset.

---

## Features

- Recommends movies based on similarity of tags.
- Uses **TF-IDF vectorization** for better weighting of unique keywords.
- Interactive **Streamlit web app** interface.
- Notebook included for **data exploration and preprocessing**.

---

## Dataset

- Based on [TMDB 5000 Movies dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata).
- Preprocessed to create a `tags` column combining genres, keywords, cast, and crew.
- Saved data files:
  - `movies_dict.pkl` — contains movie metadata.
  - `similarity.pkl` — precomputed cosine similarity matrix for recommendations.

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```

2. Create a virtual environment (optional but recommended):
```bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:
```bash
Copy code
pip install -r requirements.txt
```

4. Running the App
```bash
Copy code
streamlit run app.py
```

5. Open the link shown in the terminal to interact with the app.

6. Select a movie from the dropdown to get recommendations.

---

## Repository Structure

my-movie-recommender/<br>
│<br>
├─ app.py           # Streamlit app (main entry)<br>
├─ notebook.ipynb   # Data exploration & preprocessing<br>
├─ requirements.txt # Python dependencies<br>
├─ README.md<br>
└─ .gitignore<br>

---

## Usage
-> Run notebook.ipynb first and then, app.py. Two files calles movies_dict.pkl & simi.pkl will be created which is needed to run the app.py(could not be included due to storage limitations).<br>
-> Choose a movie from the dropdown.<br>
-> Get top 5 recommended movies with posters.<br>

---

## Quick View
<img width="1919" height="1016" alt="image" src="https://github.com/user-attachments/assets/a0c30616-0f34-4b70-b72e-bb6add5df846" />

---

## License
This project is open-source under the MIT License.

---

## Contact
Developed with ❤️ by Rujula Malhotra
GitHub: https://github.com/rm-888


