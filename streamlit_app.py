import streamlit as st
import random

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

st.text(st.session_state.quote)
col1, col2 = st.columns(2)

with col1:
    if st.button("Generate Quote"):
        choose_quote()

with col2:
    st.text("")  # Adding some space above the button
    st.button("Copy to Clipboard")
    st.write(
        f'<textarea id="quote-text" style="opacity:0;">{st.session_state.quote}</textarea><script>document.getElementById("quote-text").select();document.execCommand("copy");</script>',
        unsafe_allow_html=True,
    )
