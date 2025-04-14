import streamlit as st 


# Creating UI :
st.title("My first Project")
st.write("Lets play a game of complete the sentence.")
st.write("***Coding is amazing. I built a ________ _______ that can _______ .***")

# get user input :
adjective = st.text_input("Enter an adjective:") # Intelligent
noun = st.text_input("Enter a noun:") # robot
verb = st.text_input("Enter a verb:") # dance


 # complete the sentence :
if st.button("generate"):
     create_sentence =f"Coding is amazing. I built a {adjective} {noun} that can {verb}"
     st.subheader("Here is your complete sentence")
     st.write(create_sentence)