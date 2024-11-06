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



# Initialize session state variables
if 'started' not in st.session_state:
    st.session_state.started = False
if 'current_symbol' not in st.session_state:
    st.session_state.current_symbol = None
if 'current_feature' not in st.session_state:
    st.session_state.current_feature = None
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""
if 'completed_symbols' not in st.session_state:
    st.session_state.completed_symbols = set()
if 'remaining_features' not in st.session_state:
    st.session_state.remaining_features = []
if 'ready_for_next_symbol' not in st.session_state:
    st.session_state.ready_for_next_symbol = False

# Function to start or reset the quiz
def start_quiz():
    st.session_state.started = True
    st.session_state.score = 0
    st.session_state.attempts = 0
    st.session_state.completed_symbols = set()
    st.session_state.feedback = ""
    st.session_state.ready_for_next_symbol = False
    # Select a new symbol and load its first feature
    st.session_state.current_symbol, st.session_state.remaining_features = select_new_symbol()
    if st.session_state.remaining_features:
        st.session_state.current_feature = st.session_state.remaining_features.pop(0)

# Function to select a new symbol that hasn't been completed yet
def select_new_symbol():
    available_symbols = [symbol for symbol in ipa_features.keys() if symbol not in st.session_state.completed_symbols]
    if not available_symbols:
        return None, []  # No symbols left to practice
    symbol = random.choice(available_symbols)
    features = list(ipa_features[symbol].keys())
    return symbol, features

# Function to load the next feature for the current symbol
def load_next_feature():
    if st.session_state.remaining_features:
        st.session_state.current_feature = st.session_state.remaining_features.pop(0)
    else:
        # Mark the current symbol as completed and enable "Next Symbol" button
        st.session_state.completed_symbols.add(st.session_state.current_symbol)
        st.session_state.ready_for_next_symbol = True

# Start or Reset Button
st.button("Start/Reset Quiz", on_click=start_quiz)

# Check if the quiz has been started
if st.session_state.started:
    # Check if there are symbols left to practice
    if st.session_state.current_symbol:
        st.write(f"We'll practice with /{st.session_state.current_symbol}/ sound. Click to proceed.")

        # Show feature options for the current feature
        if st.session_state.current_feature:
            feature = st.session_state.current_feature
            correct_value = ipa_features[st.session_state.current_symbol][feature]
            
            st.write(f"Does the '{feature}' feature of /{st.session_state.current_symbol}/ have a positive or negative value?")
            col1, col2 = st.columns(2)

            # Option buttons for the feature
            with col1:
                if st.button(f"[+{feature}]") and not st.session_state.ready_for_next_symbol:
                    st.session_state.attempts += 1
                    if correct_value == '+':
                        st.session_state.score += 1
                        st.session_state.feedback = "Correct!"
                    else:
                        st.session_state.feedback = "Incorrect!"
                    load_next_feature()
            with col2:
                if st.button(f"[-{feature}]") and not st.session_state.ready_for_next_symbol:
                    st.session_state.attempts += 1
                    if correct_value == '-':
                        st.session_state.score += 1
                        st.session_state.feedback = "Correct!"
                    else:
                        st.session_state.feedback = "Incorrect!"
                    load_next_feature()

            # Display feedback
            if st.session_state.feedback:
                st.write(st.session_state.feedback)

            # Display score and attempts
            st.write(f"Score: {st.session_state.score}")
            st.write(f"Attempts: {st.session_state.attempts}")

            # Show "Next Symbol" button only when all features of the current symbol are completed
            if st.session_state.ready_for_next_symbol:
                if st.button("Next Symbol"):
                    st.session_state.current_symbol, st.session_state.remaining_features = select_new_symbol()
                    st.session_state.feedback = ""
                    st.session_state.ready_for_next_symbol = False
                    if st.session_state.remaining_features:
                        st.session_state.current_feature = st.session_state.remaining_features.pop(0)
                    else:
                        st.session_state.feedback = "You've completed all the symbols!"
    else:
        st.write("You've completed all the symbols!")
