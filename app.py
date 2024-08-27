import streamlit as st
import pickle
import pandas as pd
import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()
TMDB_API_KEY = os.getenv('TMDB_API_KEY')

# Load the sentiment analysis model
model = pickle.load(open('project3-sentiment-analysis.pkl', 'rb'))

# TMDb API configuration
BASE_URL = 'https://api.themoviedb.org/3'

def get_movie_details(movie_title):
    search_url = f"{BASE_URL}/search/movie"
    params = {
        'api_key': TMDB_API_KEY,
        'query': movie_title
    }
    response = requests.get(search_url, params=params)
    data = response.json()
    if data['results']:
        movie_id = data['results'][0]['id']
        poster_path = data['results'][0]['poster_path']
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
        return movie_id, poster_url
    return None, None

def get_movie_reviews(movie_id):
    reviews_url = f"{BASE_URL}/movie/{movie_id}/reviews"
    params = {'api_key': TMDB_API_KEY}
    response = requests.get(reviews_url, params=params)
    data = response.json()
    return [review['content'] for review in data['results']]

def get_similar_movies(movie_id):
    similar_url = f"{BASE_URL}/movie/{movie_id}/similar"
    params = {
        'api_key': TMDB_API_KEY
    }
    response = requests.get(similar_url, params=params)
    data = response.json()
    if 'results' in data:
        similar_movies = [(movie['title'], f"https://image.tmdb.org/t/p/w200{movie['poster_path']}") for movie in data['results'][:5]]  # Get top 5 similar movies
        return similar_movies
    return None

def plot_sentiment_summary(sentiments):
    sentiment_counts = pd.Series(sentiments).value_counts(normalize=True) * 100
    positive_percentage = sentiment_counts.get('positive', 0)
    negative_percentage = sentiment_counts.get('negative', 0)
    
    return positive_percentage, negative_percentage

# Streamlit app
st.set_page_config(page_title="Movie Sentiment Analyzer", layout="wide")

st.title("🎬 Cinematic AI")

# User input for movie title
movie_title = st.text_input("Enter a movie title:")

if movie_title:
    # Get the movie details from the TMDb API
    movie_id, poster_url = get_movie_details(movie_title)
    
    if movie_id:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("### Movie Poster")
            if poster_url:
                st.image(poster_url, caption=f"{movie_title}", width=200)  # Smaller movie poster
        
        with col2:
            st.markdown("### Sentiment Summary")
            reviews = get_movie_reviews(movie_id)
            if reviews:
                sentiments = model.predict(reviews)
                positive_percentage, negative_percentage = plot_sentiment_summary(sentiments)
                
                st.write(f"Positive: {positive_percentage:.1f}%")
                st.progress(positive_percentage / 100.0)
                
                st.write(f"Negative: {negative_percentage:.1f}%")
                st.progress(negative_percentage / 100.0)
        
        st.markdown("### Recommended Movies")
        similar_movies = get_similar_movies(movie_id)
        if similar_movies:
            cols = st.columns(len(similar_movies))
            for idx, (title, poster) in enumerate(similar_movies):
                with cols[idx]:
                    if poster:
                        st.image(poster, caption=title, width=100)  # Smaller recommended posters
                    else:
                        st.write(title)
        
        st.markdown("### Individual Reviews")
        if reviews:
            for idx, review in enumerate(reviews):
                sentiment = sentiments[idx]
                st.write(f"**Review:** {review}")
                st.write(f"**Sentiment:** {sentiment}")
                st.write("---")
        else:
            st.write(f"No reviews found for '{movie_title}'.")
    else:
        st.write(f"Movie '{movie_title}' not found.")
