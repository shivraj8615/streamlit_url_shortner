import pyshorteners
import streamlit as st
path = "/home/p/shiv/streamlit/url_img.png"
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


