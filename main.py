import streamlit as st
import pickle

st.header("Movie Recommendation System")
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
selectMovies = st.text_input("Enter Movies Title")

def recommend_similar_movies(movie_name):
    calculatedMovies = []
    index = movies[movies['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    for i in distances[1:10]:
        calculatedMovies.append(movies.iloc[i[0]].title)
    return calculatedMovies


if selectMovies:
    try:
        displayMovies = recommend_similar_movies(selectMovies)
        c1, c2, c3 = st.columns(3)
        c4, c5, c6 = st.columns(3)
        c7, c8, c9 = st.columns(3)
        with c1:
            st.info(displayMovies[0])
        with c2:
            st.info(displayMovies[1])
        with c3:
            st.info(displayMovies[2])
        with c4:
            st.warning(displayMovies[3])
        with c5:
            st.warning(displayMovies[4])
        with c6:
            st.warning(displayMovies[5])
        with c7:
            st.error(displayMovies[6])
        with c8:
            st.error(displayMovies[7])
        with c9:
            st.error(displayMovies[8])
    except:
        


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer:before{
            content:"Developed By-Roshan Adhikari(19031101)";
            display:block;
            color:#FF5349;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
