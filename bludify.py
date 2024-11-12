
import streamlit as st

st.title("bludify.com!!!!")
st.header("from bluds, to bluds")
st.subheader("the best music app for bluds")

# Caminho do arquivo com string raw
m1 = st.button("what a sigma")
m2 = st.button("KABOOM!")
m3 = st.button("blue lobster")

if m1:
    audio_url = "https://drive.google.com/uc?export=download&id=1pYetLCMcfWIX39QbY6zD81A7KbZvahab"
    audio_html = f'<audio controls><source src="{audio_url}" type="audio/mpeg"></audio>'
    st.markdown(audio_html, unsafe_allow_html=True)

if m2:
    audio_url = "https://drive.google.com/uc?export=download&id=19WydQkhrIG7rcmXEuuBWrU8oOv1yMJjg"
    audio_html = f'<audio controls><source src="{audio_url}" type="audio/mpeg"></audio>'
    st.markdown(audio_html, unsafe_allow_html=True)

if m3:
    audio_url = "https://drive.google.com/uc?export=download&id=17cVDPjhkxLdU1mDwrJROXAend-J-ViO-"
    audio_html = f'<audio controls><source src="{audio_url}" type="audio/mpeg"></audio>'
    st.markdown(audio_html, unsafe_allow_html=True)
