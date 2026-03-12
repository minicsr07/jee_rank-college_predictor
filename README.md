# 🎓 JEE Rank & NIT College Predictor

![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)

A Machine Learning powered web application that predicts **JEE Main rank** based on marks and percentile, and recommends **possible NIT colleges and branches** using historical cutoff data.

---

# Live App

Try the deployed app here:

 https://jeerank-collegepredictor-5sspkpamjhighgg3ysv2yv.streamlit.app/

---

# Project Overview

This project uses historical **JEE Main marks, percentile, and rank data** to train a machine learning model that predicts expected rank.

Based on the predicted rank, the system recommends **possible NIT colleges and branches** using previous years’ cutoff data.

This project demonstrates:

- Machine Learning model training
- Data analysis and preprocessing
- Recommendation systems
- Web application deployment using Streamlit
- GitHub project management

---

# Features

 Predict JEE Rank using ML model  
 Recommend NIT colleges based on predicted rank  
 Category and quota filtering  
 Interactive Streamlit web interface  
 Percentile vs Rank visualization  
 Fully deployed web application

---

# Tech Stack

## Programming Language
- Python

## Libraries
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly

## Tools
- Google Colab
- GitHub
- Streamlit Cloud

---

# Datasets Used

Two datasets were used in this project.

### 1️ JEE Marks–Percentile–Rank Dataset
Used to train the machine learning model that predicts JEE rank.

### 2️ NIT College Cutoff Dataset
Used to recommend NIT colleges and branches based on predicted rank.

---

# Project Structure

```
jee-rank-college-predictor
│
├── streamlit_jee_rank_app.py
├── rank_model.pkl
├── jee_rank_predictor.ipynb
├── jee_marks_percentile_rank_2009_2026.csv
├── jee_college_cutoffs_nits.csv
├── requirements.txt
└── README.md
```

---

# How to Run Locally

Clone the repository

```
git clone https://github.com/minicsr07/jee-rank-college-predictor.git
```

Navigate to the project folder

```
cd jee-rank-college-predictor
```

Install dependencies

```
pip install -r requirements.txt
```

Run the Streamlit app

```
streamlit run streamlit_jee_rank_app.py
```

---

# Example Output

The app predicts the expected rank and recommends possible NIT colleges based on:

- Marks
- Percentile
- Category
- Quota
- Total candidates

---

# Author

**Charan**

B.Tech CSE  
Interested in **Machine Learning, Data Science, and AI**

---
