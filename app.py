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
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'next_requested' not in st.session_state:
    st.session_state.next_requested = False

# Function to start or reset the quiz
def start_quiz():
    st.session_state.started = True
    st.session_state.score = 0
    st.session_state.attempts = 0
    st.session_state.completed_symbols = set()
    st.session_state.feedback = ""
    st.session_state.answered = False
    st.session_state.next_requested = False
    select_new_symbol()

# Function to select a new symbol and reset its features
def select_new_symbol():
    available_symbols = [symbol for symbol in ipa_features if symbol not in st.session_state.completed_symbols]
    if not available_symbols:
        st.session_state.current_symbol = None
        st.session_state.remaining_features = []
    else:
        st.session_state.current_symbol = random.choice(available_symbols)
        st.session_state.remaining_features = list(ipa_features[st.session_state.current_symbol].keys())
        st.session_state.current_feature = st.session_state.remaining_features.pop(0)
        st.session_state.feedback = ""
        st.session_state.answered = False

# Function to handle answer checking
def check_answer(user_choice):
    if not st.session_state.answered:  # Only proceed if the feature hasn't been answered yet
        correct_value = ipa_features[st.session_state.current_symbol][st.session_state.current_feature]
        st.session_state.attempts += 1
        if user_choice == correct_value:
            st.session_state.score += 1
            st.session_state.feedback = "😍 Correct!"
        else:
            st.session_state.feedback = "😓 Oh, no!"
        st.session_state.answered = True

# Function to load the next feature or symbol in a single click
def load_next_feature():
    if st.session_state.remaining_features:
        st.session_state.current_feature = st.session_state.remaining_features.pop(0)
        st.session_state.feedback = ""  # Clear feedback only when loading a new question
        st.session_state.answered = False
    else:
        st.session_state.completed_symbols.add(st.session_state.current_symbol)
        select_new_symbol()

# Start/Reset Quiz Button
if st.button("Start/Reset Quiz"):
    start_quiz()

# Apply custom CSS for button colors
st.markdown("""
    <style>
        .stButton > button:first-child {
            width: 100px;
        }
        .positive-button button {
            background-color: #4CAF50; /* Green */
            color: white;
        }
        .negative-button button {
            background-color: #f44336; /* Red */
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Quiz flow
if st.session_state.started:
    # Check if there are symbols left to practice
    if st.session_state.current_symbol:
        st.markdown(f"### 🍃 Q: Feature [ {st.session_state.current_feature} ] of / {st.session_state.current_symbol} /?")

        # Display answer buttons for the feature only if it hasn't been answered yet
        if not st.session_state.answered:
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"[+{st.session_state.current_feature}]", key="positive", help="Positive Feature", use_container_width=True):
                    check_answer('+')
            with col2:
                if st.button(f"[-{st.session_state.current_feature}]", key="negative", help="Negative Feature", use_container_width=True):
                    check_answer('-')

        # Display feedback
        if st.session_state.feedback:
            st.write(st.session_state.feedback)

        # Display score and attempts
        st.write(f"Score: {st.session_state.score}")
        st.write(f"Attempts: {st.session_state.attempts}")

        # Button to proceed to the next feature or symbol
        if st.session_state.answered:
            if st.button("Next Feature / Symbol"):
                load_next_feature()  # Call load_next_feature to immediately update the question
    else:
        st.write("You've completed all the symbols!")
