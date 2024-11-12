import streamlit as st

st.title("bludify.com!!!!")
st.header("from bluds, to bluds")
st.subheader("the best music app for bluds")

# Consider using a cloud storage provider with direct hotlinking if CORS is an issue
audio_urls = {
    "what a sigma": "https://drive.google.com/file/d/19WydQkhrIG7rcmXEuuBWrU8oOv1yMJjg/view?usp=sharing",  # Replace with your actual URL
    "KABOOM!": "https://drive.google.com/file/d/1pYetLCMcfWIX39QbY6zD81A7KbZvahab/view?usp=drive_link",
    "blue lobster": "https://drive.google.com/file/d/17cVDPjhkxLdU1mDwrJROXAend-J-ViO-/view?usp=drive_link"
}

m1 = st.button("what a sigma")
m2 = st.button("KABOOM!")
m3 = st.button("blue lobster")

if m1:
    audio_url = audio_urls["what a sigma"]
    audio_html = f'<audio controls><source src="{audio_url}" type="audio/mpeg"></audio>'
    st.markdown(audio_html, unsafe_allow_html=True)

if m2:
    audio_url = audio_urls["KABOOM!"]
    audio_html = f'<audio controls><source src="{audio_url}" type="audio/mpeg"></audio>'
    st.markdown(audio_html, unsafe_allow_html=True)

if m3:
    audio_url = audio_urls["blue lobster"]
    audio_html = f'<audio controls><source src="{audio_url}" type="audio/mpeg"></audio>'
    st.markdown(audio_html, unsafe_allow_html=True)
