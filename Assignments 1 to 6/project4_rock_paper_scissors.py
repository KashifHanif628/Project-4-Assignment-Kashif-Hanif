import streamlit as st 
import random 
"""The winner will get the cash prizes and much more....!"""
def Winner(users,computer):
    if users == computer:
        return"Its a tie"
    elif (users == 'Rock' and computer == 'Scissors') or \
         (users == 'Paper' and computer == 'Rock') or \
         (users == 'Scissors' and computer == 'Paper') :
         return "You win"   
    else:
        return "Computers Win The Game"
st.title("Lets Check the results")
#user selection  :
tools = ['Rock', 'Paper', 'Scissors']
users = st.selectbox("Choose your move:", tools)  # User selects their move
computer = random.choice(tools)  # Computer selects randomly

if st.button("Play"):
    st.write(f"User Choice : {users}")
    st.write(f"computer Choice : {computer}")
    result_of_game = Winner(users,computer)
    st.subheader(result_of_game)   