import streamlit as st
import langchain_helper

st.title("Movie Name Generator")

language = st.sidebar.selectbox("Pick a Language", ("English", "Telugu", "Hindi", "Tamil", "Malayalam","Chineese", "French", "Spanish","Bengali", "Turkish"))

if language:
    response = langchain_helper.generate_movie_name_and_tags(language)
    st.header(f"Movie Name in English: {response['movie_name_english'].strip()}")
    st.header(f"Movie Name in {language}: {response['movie_name_translated'].strip()}")
    movie_tags = response['movie_tags'].strip().split(",")
    st.write("**Movie Tags**")
    for item in movie_tags:
        st.write("-", item.strip())
