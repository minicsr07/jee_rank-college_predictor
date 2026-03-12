
import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

# Page settings
st.set_page_config(
    page_title="JEE Rank & NIT Predictor",
    page_icon="🎓",
    layout="wide"
)

# Load model
model = pickle.load(open("rank_model.pkl","rb"))

# Load datasets
college_df = pd.read_csv("jee_college_cutoffs_nits.csv")
rank_df = pd.read_csv("jee_marks_percentile_rank_2009_2026.csv")

# Title
st.title("🎓 JEE Rank & NIT College Predictor")

st.image("https://upload.wikimedia.org/wikipedia/commons/7/7d/Joint_Entrance_Examination_%28Main%29_logo.png", width=120)

st.markdown(
'''
Predict your **expected JEE rank** and see possible **NIT colleges** based on your marks and percentile.
'''
)

# Sidebar Inputs
st.sidebar.header("Enter Your Details")

marks = st.sidebar.number_input("Marks", min_value=0.0, max_value=300.0)
percentile = st.sidebar.number_input("Percentile", min_value=0.0, max_value=100.0)

category = st.sidebar.selectbox(
    "Category",
    ["General","OBC-NCL","SC","ST","EWS"]
)

quota = st.sidebar.selectbox(
    "Quota",
    ["Other State","Home State"]
)

year = st.sidebar.number_input("Year", value=2026)
candidates = st.sidebar.number_input("Total Candidates", value=1200000)

# Prediction
if st.sidebar.button("Predict Rank"):

    sample = [[marks, percentile, year, candidates]]

    rank = model.predict(sample)
    rank = int(rank[0])

    st.subheader("Predicted Rank")

    st.success(f"Estimated Rank: **{rank}**")

    # College recommendations
    possible = college_df[
        (college_df["Opening_Rank"] <= rank) &
        (college_df["Closing_Rank"] >= rank) &
        (college_df["Category"] == category) &
        (college_df["Quota"] == quota)
    ]

    st.subheader("Possible NIT Colleges")

    st.dataframe(
        possible[["Institute","Branch","Closing_Rank"]]
        .head(10)
        .reset_index(drop=True)
    )

# Visualization Section
st.subheader("Percentile vs Rank Trend")

fig = px.scatter(
    rank_df,
    x="Percentile",
    y="Rank",
    title="JEE Percentile vs Rank",
    opacity=0.6
)

st.plotly_chart(fig, use_container_width=True)
