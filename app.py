# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c62dfb3048fed2c221f2b1ad66215eb4&language=en-US'.format(movie_id))
#     data = response.json()
#     print(data)
#     return "http://image.tmdb.org/t/p/w500/" + data['poster_path']
#
#
# st.title('Movie Recommender System')
#
# movies_dict = pickle.load(open('.venv/movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('.venv/similarity_metrics.pkl','rb'))
# select_movie_name = st.selectbox(
#     'How would you like to be contacted?',
#     movies['title'].values)
#
# def recommend(movie):
#   movie_index = movies[movies['title'] == movie].index[0]
#   distances = similarity[movie_index]
#   movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
#
#   recommend_movies = []
#   recommended_movies_poster=[]
#
#   for i in movies_list:
#       movie_id = i[0]
#       # fetch proster from api
#       recommend_movies.append(movies.iloc[i[0]].title)
#       recommended_movies_poster.append(fetch_poster(movie_id))
#   return recommend_movies,recommended_movies_poster
#
# if st.button('Recommend'):
#     names,posters=recommend(select_movie_name)
#
#     col1, col2, col3,col4,col5 = st.columns(3)
#
#     with col1:
#         st.header("A cat")
#         st.image("https://static.streamlit.io/examples/cat.jpg")
#
#     with col2:
#         st.header("A dog")
#         st.image("https://static.streamlit.io/examples/dog.jpg")
#
#     with col3:
#         st.header("An owl")
#         st.image("https://static.streamlit.io/examples/owl.jpg")
#
#     with col4:
#         st.header("An owl")
#         st.image("https://static.streamlit.io/examples/owl.jpg")
#
#     with col5:
#         st.header("An owl")
#         st.image("https://static.streamlit.io/examples/owl.jpg")
#
#
# # st.write('You selected:', option)


import streamlit as st
import pickle
import pandas as pd
import requests

# Function to fetch the poster URL
def fetch_poster(movie_id):
    try:
        response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=c62dfb3048fed2c221f2b1ad66215eb4&language=en-US')
        data = response.json()
        # Check if the 'poster_path' exists in the data
        if 'poster_path' in data:
            return f"http://image.tmdb.org/t/p/w500/{data['poster_path']}"
        else:
            # Return a default image if 'poster_path' is not found
            return "https://via.placeholder.com/500x750?text=No+Image"
    except Exception as e:
        # Handle exceptions and return a default image
        print(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image"

st.title('Movie Recommender System')

# Load movie data and similarity metrics
movies_dict = pickle.load(open('.venv/movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('.venv/similarity_metrics.pkl', 'rb'))

# User input for movie selection
select_movie_name = st.selectbox('Select a movie:', movies['title'].values)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # Adjust to match the actual column name for movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommend_movies, recommended_movies_poster

if st.button('Recommend'):
    names, posters = recommend(select_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

