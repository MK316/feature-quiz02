import streamlit as st
import random

# IPA features dictionary with full feature names
ipa_features = {
    'p': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '-', 'anterior': '+', 'continuant': '-', 'nasal': '-', 'strident': '-', 'lateral': '-', 'delayed release': '-', 'voice': '-'},
    'b': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '-', 'anterior': '+', 'continuant': '-', 'nasal': '-', 'strident': '-', 'lateral': '-', 'delayed release': '-', 'voice': '+'},
    't': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '+', 'anterior': '+', 'continuant': '-', 'nasal': '-', 'strident': '-', 'lateral': '-', 'delayed release': '-', 'voice': '-'},
    'd': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '+', 'anterior': '+', 'continuant': '-', 'nasal': '-', 'strident': '-', 'lateral': '-', 'delayed release': '-', 'voice': '+'},
    'k': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '-', 'anterior': '-', 'continuant': '-', 'nasal': '-', 'strident': '-', 'lateral': '-', 'delayed release': '-', 'voice': '-'},
    'g': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '-', 'anterior': '-', 'continuant': '-', 'nasal': '-', 'strident': '-', 'lateral': '-', 'delayed release': '-', 'voice': '+'},
    'tʃ': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '+', 'anterior': '-', 'continuant': '-', 'nasal': '-', 'strident': '+', 'lateral': '-', 'delayed release': '+', 'voice': '-'},
    'dʒ': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '+', 'anterior': '-', 'continuant': '-', 'nasal': '-', 'strident': '+', 'lateral': '-', 'delayed release': '+', 'voice': '+'},
    'f': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '-', 'anterior': '-', 'continuant': '+', 'nasal': '-', 'strident': '+', 'lateral': '-', 'delayed release': '-', 'voice': '-'},
    'v': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '-', 'anterior': '-', 'continuant': '+', 'nasal': '-', 'strident': '+', 'lateral': '-', 'delayed release': '-', 'voice': '+'},
    'θ': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '-', 'anterior': '+', 'continuant': '+', 'nasal': '-', 'strident': '-', 'lateral': '-', 'delayed release': '-', 'voice': '-'},
    'ð': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '-', 'anterior': '+', 'continuant': '+', 'nasal': '-', 'strident': '-', 'lateral': '-', 'delayed release': '-', 'voice': '+'},
    's': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '+', 'anterior': '+', 'continuant': '+', 'nasal': '-', 'strident': '+', 'lateral': '-', 'delayed release': '-', 'voice': '-'},
    'z': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '+', 'anterior': '+', 'continuant': '+', 'nasal': '-', 'strident': '+', 'lateral': '-', 'delayed release': '-', 'voice': '+'},
    'ʃ': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '+', 'anterior': '-', 'continuant': '+', 'nasal': '-', 'strident': '+', 'lateral': '-', 'delayed release': '-', 'voice': '-'},
    'ʒ': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '+', 'anterior': '-', 'continuant': '+', 'nasal': '-', 'strident': '+', 'lateral': '-', 'delayed release': '-', 'voice': '+'},
    'h': {'syllabic': '-', 'consonantal': '+', 'sonorant': '-', 'coronal': '-', 'anterior': '-', 'continuant': '+', 'nasal': '-', 'strident': '-', 'lateral': '-', 'delayed release': '-', 'voice': '-'},
    'm': {'syllabic': '-', 'consonantal': '+', 'sonorant': '+', 'coronal': '-', 'anterior': '+', 'continuant': '-', 'nasal': '+', 'strident': '-', 'lateral': '-', 'delayed release': '-', 'voice': '+'},
    'n': {'syllabic': '-', 'consonantal': '+', 'sonorant': '+', 'coronal': '+', 'anterior': '+', 'continuant': '-', 'nasal': '+', 'strident': '-', 'lateral': '-', 'delayed release': '-', 'voice': '+'},
    'ŋ': {'syllabic': '-', 'consonantal': '+', 'sonorant': '+', 'coronal': '-', 'anterior': '-', 'continuant': '-', 'nasal': '+', 'strident': '-', 'lateral': '-', 'delayed release': '-', 'voice': '+'},
    'l': {'syllabic': '-', 'consonantal': '+', 'sonorant': '+', 'coronal': '+', 'anterior': '+', 'continuant': '-', 'nasal': '-', 'strident': '-', 'lateral': '+', 'delayed release': '-', 'voice': '+'},
    'r': {'syllabic': '-', 'consonantal': '+', 'sonorant': '+', 'coronal': '+', 'anterior': '+', 'continuant': '+', 'nasal': '-', 'strident': '-', 'lateral': '-', 'delayed release': '-', 'voice': '+'},
    'j': {'syllabic': '-', 'consonantal': '-', 'sonorant': '+', 'coronal': '+', 'anterior': '-', 'continuant': '+', 'nasal': '-', 'strident': '-', 'lateral': '-', 'delayed release': '-', 'voice': '+'},
    'w': {'syllabic': '-', 'consonantal': '-', 'sonorant': '+', 'coronal': '-', 'anterior': '-', 'continuant': '+', 'nasal': '-', 'strident': '-', 'lateral': '-', 'delayed release': '-', 'voice': '+'}
}


# Streamlit app setup
st.title("IPA Features Quiz")
st.header("Guess the feature of the symbol")

# State management to keep track of scores and attempts
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

# Select a random symbol and a random feature to ask about
symbol, features = random.choice(list(ipa_features.items()))
feature, value = random.choice(list(features.items()))

# Display the symbol and question
st.subheader(f"Symbol: {symbol}")
question = f"Does the '{feature}' feature of this symbol have a positive or negative value?"
st.write(question)

# Buttons for user to guess the feature value
col1, col2 = st.columns(2)
with col1:
    if st.button(f"[+{feature}]"):
        # Check if user's guess is correct
        if value == '+':
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error("Incorrect!")
        st.session_state.attempts += 1

with col2:
    if st.button(f"[-{feature}]"):
        if value == '-':
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error("Incorrect!")
        st.session_state.attempts += 1

# Display score and number of attempts
st.write(f"Score: {st.session_state.score}")
st.write(f"Attempts: {st.session_state.attempts}")

# Button to reload for a new question
if st.button("Next Symbol"):
    st.experimental_rerun()
