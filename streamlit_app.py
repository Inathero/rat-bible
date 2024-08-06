import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import random
import rat_quotes as rat

# Header
st.title('The Rat Bible')

# Embed image
st.markdown("<div style='text-align: center;'><img src='https://my.minmatar.org/images/fleet-logo.svg' style='width:200px;'></div>", unsafe_allow_html=True)

# Separator
st.markdown("---")

st.info("How to use: Copy the holy rat quote below by either clicking the clipboard icon to the right of the text box, or select all text and copy it.")

if 'quote' not in st.session_state:
    st.session_state.quote = ""

def choose_quote():
    st.session_state.quote = random.choice(rat.rat_quotes)

choose_quote()

with stylable_container(
    "codeblock",
    """
    code {
        white-space: pre-wrap !important;
    }
    """,
):
    st.code(st.session_state.quote)

if st.button("Generate Quote"):
    choose_quote()
