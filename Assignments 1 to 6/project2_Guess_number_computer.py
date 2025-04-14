# Project 2 Guess the number game python project (computer)

import streamlit as st
import random

st.title("🎯 Number Guessing Game")
st.write("***Guess the correct number between 0 and 99 to win Rs. 1000/-***")

# Initialize session state
if "guess_number" not in st.session_state:
    st.session_state.guess_number = random.randint(0, 99)
    st.session_state.game_over = False

# Input from user
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=0, max_value=99, step=1)
    if st.button("Submit Guess"):
        if guess < st.session_state.guess_number:
            st.warning("Sorry, guess again. Too low.")
        elif guess > st.session_state.guess_number:
            st.warning("Sorry, guess again Too high.")
        else:
            st.success(f"🎉 Congrats! You guessed the correct number: {st.session_state.guess_number}")
            st.balloons()
            st.success("Here is your winning prize of Rs. 1000/-")
            st.session_state.game_over = True
else:
    if st.button("Play Again"):
        st.session_state.guess_number = random.randint(0, 99)
        st.session_state.game_over = False
