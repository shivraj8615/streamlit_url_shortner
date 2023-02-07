import pyshorteners
import streamlit as st
path = "https://github.com/shivraj8615/streamlit_url_shortner/blob/main/url_img.png"
st.image(path)
heading = st.write("# URL Shortner")
st.header(heading)

input_url = st.text_input("")

if st.button('Submit'):
    link = input_url
    shorteners = pyshorteners.Shortener()
    shortlink = shorteners.tinyurl.short(link)
    st.write(shortlink)
else:
    st.write("Write a proper link")


