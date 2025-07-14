import streamlit as st
import pickle


with open('model.pkl', 'rb') as f:
    nb = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Streamlit app UI
st.title("📰 Fake News Detector")

headline = st.text_input("Enter a news headline:")

if st.button("Check"):
    if headline:
        headline_tfidf = vectorizer.transform([headline])
        prediction = nb.predict(headline_tfidf)[0]
        proba = nb.predict_proba(headline_tfidf)[0]

        label = "Real ✅" if prediction == 1 else "Fake 🚫"
        st.subheader(f"Prediction: {label}")
        st.write(f"Probability: Fake {proba[0]:.2%} | Real {proba[1]:.2%}")
    else:
        st.warning("Please enter a headline.")
