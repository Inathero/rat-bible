import streamlit as st
import random
import rat_quotes as rat

# Header
st.title('The Rat Bible')

# Embed image
st.markdown("<div style='text-align: center;'><img src='https://my.minmatar.org/images/fleet-logo.svg' style='width:200px;'></div>", unsafe_allow_html=True)

# Separator
st.markdown("---")

st.text("How to use: Copy the holy rat quote below by either clicking the clipboard icon to the right of the text box, or select all text and copy it.")
# Text and buttons

if 'quote' not in st.session_state:
    st.session_state.quote = ""

def choose_quote():
    st.session_state.quote = random.choice(rat.rat_quotes)

choose_quote()

st.code(st.session_state.quote)

# col1, col2 = st.columns(2)

# with col1:
if st.button("Generate Quote"):
    choose_quote()

# with col2:
#     st.text("")  # Adding some space above the button
#     if st.button("Copy to Clipboard"):
#         st.markdown(f'<input type="text" value="{st.session_state.quote}" id="quote-input" style="position: absolute; left: -1000px;">', unsafe_allow_html=True)
#         st.markdown(
#             """
#             <script>
#                 var copyText = document.getElementById("quote-input");
#                 copyText.select();
#                 copyText.setSelectionRange(0, 99999); /* For mobile devices */
#                 document.execCommand("copy");
#             </script>
#             """,
#             unsafe_allow_html=True,
#         )
