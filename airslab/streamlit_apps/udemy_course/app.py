import streamlit as st

st.title("Streamlit Basic Course")
st.header("This is header")
st.subheader("This is subheader")
st.text("This is text")
st.write("This is WRITE text")
st.markdown("# This is markdown")
st.header("This is linkable Text and Links")
st.markdown("[Streamlit](https://www.streamlit.io/)")

url_link = "https://citikot.github.io"
st.markdown(url_link)

st.header("HTML (Style)")
# Custom Color/Style
html_page = """
<div style="background-color:cyan;padding:50px">
	<p style="color:cyan;font-size:50px">Enjoy Streamlit!</p>

</div>
"""
st.markdown(html_page, unsafe_allow_html=True)

# HTML (Style)
st.header("Colors")
st.success("Success!")

st.info("Information")
st.warning("This is a warning")
st.error("This is an error")

st.header("Images, Video and Audio")
# Images
from PIL import Image

img = Image.open("RML_Logo.png")
st.image(img, width=300, caption="My Image")


# Video
video_file = open("SampleVideo_1280x720_1mb.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)