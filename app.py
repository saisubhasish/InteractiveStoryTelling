import requests
import streamlit as st

# Set the FastAPI server URL
BASE_URL = "http://localhost:8000"

st.title("Engaging Interactive Storytelling with AI")

# Initialize session state for story title and introduction
if "story_title" not in st.session_state:
    st.session_state["story_title"] = ""
if "story_introduction" not in st.session_state:
    st.session_state["story_introduction"] = ""

# Story Introduction
st.header("Generate Story Introduction")
st.session_state["story_title"] = st.text_input("Enter the title of your story:", value=st.session_state["story_title"])

if st.button("Generate Introduction"):
    if st.session_state["story_title"]:
        response = requests.post(f"{BASE_URL}/story_introduction/", json={"story_title": st.session_state["story_title"]})
        if response.status_code == 200:
            st.session_state["story_introduction"] = response.json()
            st.subheader("Story Introduction")
            st.write(st.session_state["story_introduction"])
        else:
            st.error("Failed to get story introduction: " + response.text)
    else:
        st.error("Please enter a story title.")

# Storytelling
st.header("Generate Full Story")
st.session_state["story_introduction"] = st.text_area("Enter the story introduction(Modify if needed):", value=st.session_state["story_introduction"])

if st.button("Generate Story"):
    if st.session_state["story_title"] and st.session_state["story_introduction"]:
        response = requests.post(f"{BASE_URL}/story_telling/", json={"story_title": st.session_state["story_title"], "story_introduction": st.session_state["story_introduction"]})
        if response.status_code == 200:
            story = response.json()
            st.subheader("Full Story")
            st.write(story)
        else:
            st.error("Failed to get story: " + response.text)
    else:
        st.error("Please enter both a story title and a story introduction.")
