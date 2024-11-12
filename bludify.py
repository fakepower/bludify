import streamlit as st

st.title("bludify.com!!!!")
st.header("from bluds, to bluds")
st.subheader("the best music app for bluds")

# Caminho do arquivo com string raw
m1 = st.button("what a sigma")
m2 = st.button("KABOOM!")
m3 = st.button("blue lobster")

if m1:
    audio_path = "https://drive.google.com/uc?export=download&id=1pYetLCMcfWIX39QbY6zD81A7KbZvahab"
    st.audio(audio_path)

if m2:
    audio_path = "https://drive.google.com/uc?export=download&id=19WydQkhrIG7rcmXEuuBWrU8oOv1yMJjg"
    st.audio(audio_path)

if m3:
    audio_path = "https://drive.google.com/uc?export=download&id=17cVDPjhkxLdU1mDwrJROXAend-J-ViO-"
    st.audio(audio_path)
