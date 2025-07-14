# 📰 AI-Powered Fake News Detector

# 🏆 Supporting SDG 16: Peace, Justice & Strong Institutions

# 📌 Project Overview
This project is an AI-powered web application that detects whether a news headline is likely fake or real. It aims to support UN Sustainable Development Goal 16, which promotes peace, justice, and strong institutions by tackling misinformation and its harmful effects.

# 🧠 How It Works
Dataset: Kaggle’s Fake and Real News Dataset (~44,000 samples).

Preprocessing: Headlines are cleaned, tokenized, and vectorized using TF-IDF.

Model: A simple Naive Bayes classifier was trained for binary text classification.

App: Built with Streamlit, users can input any news headline and get a prediction: Fake or Real.

# ⚙️ Tech Stack
Python

scikit-learn

Streamlit

Google Colab (for model training)

GitHub + Streamlit Community Cloud (for version control & deployment)

# 🚀 Try It Live
👉 Click here to open the app https://fake-news-detector-hgmod2ksctbd5gjdfjf3rg.streamlit.app/


# 📈 Results
The model achieved 93% accuracy

# ⚠️ Bias & Limitations
Data Bias: The model was trained on a dataset of mostly English-language, US-based news articles. It is therefore biased toward detecting fake or real news patterns common in US political and mainstream media.

Generalization: Headlines that are non-US, non-political, or written in other languages may be misclassified because the model has never seen those patterns.

Headline-Only: This tool only analyzes headlines, not full articles, which can limit accuracy since context and supporting facts are missing.

Simplicity: The model uses a simple TF-IDF + Naive Bayes approach. While lightweight and interpretable, it is less robust than advanced deep learning models.

# 🛡️ Contribution to SDG 16
By providing a simple tool to detect misinformation, this project helps individuals critically evaluate news content and supports stronger institutions by promoting transparency and accountability.

# 🔍 Future Improvements
Use more advanced models (e.g., BERT)

Add multilingual support

Expand to full article analysis

Collect real-world feedback to improve accuracy



