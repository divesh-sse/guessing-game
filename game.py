import streamlit as st
import random

# Set a random number to guess
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.guesses = 0  # Keep track of number of guesses

# Title of the app
st.title("Number Guessing Game")

# Display the current number of guesses
st.write(f"Number of guesses: {st.session_state.guesses}")

# Input box for user to enter a guess
guess = st.number_input("Guess a number between 1 and 100:", min_value=1, max_value=100)

# Button to check the guess
if st.button("Check Guess"):
    st.session_state.guesses += 1
    if guess < st.session_state.number:
        st.write("Too low! Try again.")
    elif guess > st.session_state.number:
        st.write("Too high! Try again.")
    else:
        st.write(f"Congratulations! You've guessed the number {st.session_state.number} in {st.session_state.guesses} guesses!")
        # Reset the game after correct guess
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.guesses = 0
            st.experimental_rerun()

