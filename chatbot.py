import streamlit as st

# FAQ data
faq = {
    "what is farmerskonnect": "FarmersKonnect connects farmers with buyers and agricultural resources.",
    
    "how do i register": "Click on the register button and fill in your details.",
    
    "can buyers contact farmers": "Yes, buyers can connect directly with farmers.",
    
    "is farmerskonnect free": "Yes, basic registration is free.",
    
    "what products are available": "You can find crops, livestock, and farm produce."
}

# Page title
st.title("FarmersKonnect FAQ Chatbot")

# User input
user_question = st.text_input("Ask a question")

# Chatbot response
if user_question:
    question = user_question.lower()

    if question in faq:
        st.success(faq[question])
    else:
        st.error("Sorry, I do not understand that question yet.")