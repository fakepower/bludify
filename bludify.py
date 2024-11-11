import streamlit as st
st.title("bludify.com!!!!")
st.header("from bluds, to bluds")
st.subheader("the best music app for bluds")
# Caminho do arquivo com string raw
m1 = st.button("what a sigma")
m2 = st.button("KABOOM!")
m3 = st.button("blue lobster")
if m1:
    audio_path = r"C:\Users\Luiz\Downloads\erm what the sigma original video.mp3"

    st.audio(audio_path)
if m2:
    audio_path = r"C:\Users\Luiz\Downloads\KABOOM THERE GOES YOUR TOWER (credit to harrytwinkle2929).mp3"
    st.audio(audio_path)
if m3:
    audio_path = r"C:\Users\Luiz\Downloads\Blue Lobster Jumpscare Meme Sound (HD) ｜ Toccata and Fugue in D Minor Song.mp3"
    st.audio(audio_path)


