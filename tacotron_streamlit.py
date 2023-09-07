import streamlit as st
import requests
import os
import json
from streamlit_lottie import st_lottie

# Customize the Streamlit theme
st.set_page_config(
    page_title='Text to Speech Demo',
    page_icon="🔊",
    layout="wide",
)

# Application title
st.markdown('<p style="font-size: 60px; font-weight: bold;">Text to Speech Demo</p>', unsafe_allow_html=True)

# Split the layout into two columns
col1, col2 = st.columns(2)

# Text input for entering text to convert to speech
with col1:
    text_to_transform = st.text_input('', 'On the shoulders of giants')

    get_speech2_button = st.button('🎤 Get speech', help='Click to get the speech conversion', key="get_speech",  args={'height': 60})

    get_speech_button = st.button('🎤 Get tacotron speech', help='Click to get the speech conversion', key="get_speech2",  args={'height': 60})



# Use st.sidebar to create a second page
with st.sidebar:

    # Load JSON content from the file
    with open("image_json/chatbot.json", "r") as json_file:
        json_data = json.load(json_file)

    # Display JSON content in the sidebar
    st_lottie(json_data)

    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)

    get_dummy_speech_button = st.button('😢 Get dummy speech', help='Click to get a pre-created speech conversion')


# Display the audio result
if get_speech_button:
    params = dict(text_to_transform=text_to_transform)
    tts_api_url = 'https://docker-tacotron2-2tg6hvtuea-ew.a.run.app/predict?text_to_transform='
    response = requests.get(tts_api_url, params=params)
    wav_file = response.content
    st.audio(wav_file, format="audio/wav")

if get_dummy_speech_button:
    dummy_wav_path = os.path.join("dummy_wav", 'LJ001-0010.wav')
    st.audio(dummy_wav_path, format="audio/wav")

if get_speech2_button:
    dummy_wav_path = os.path.join("wav", 'LJ001-0001.wav')
    st.audio(dummy_wav_path, format="audio/wav")
