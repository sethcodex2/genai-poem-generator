import streamlit as st
from convert import generate_image, generate_poem
st.title('A+ Poems')

title = st.text_input('Enter a poem title')
clicked = st.button('Generate Poem')


if title and clicked:
    st.image(generate_image(title))
    st.write(generate_poem(title))
