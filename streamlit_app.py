import streamlit as st
import random
import pyperclip

# Header
st.title('The Rat Bible')

# Embed image
st.markdown("<div style='text-align: center;'><img src='https://my.minmatar.org/images/fleet-logo.svg' style='width:200px;'></div>", unsafe_allow_html=True)

# Separator
st.markdown("---")

# Text and buttons
rat_quotes = [
    "Squeak squeak!",
    "Find the cheese.",
    "Avoid the trap.",
    "Scurrying through the night.",
    "Long live the Rat King!"
]

if 'quote' not in st.session_state:
    st.session_state.quote = ""

def choose_quote():
    st.session_state.quote = random.choice(rat_quotes)

def copy_to_clipboard():
    pyperclip.copy(st.session_state.quote)

# st.text(st.session_state.quote)
st_copy_to_clipboard(st.session_state.quote)

col1, col2 = st.columns(2)

with col1:
    if st.button("Generate Quote"):
        choose_quote()

with col2:
    if st.button("Copy to Clipboard"):
        copy_to_clipboard()
