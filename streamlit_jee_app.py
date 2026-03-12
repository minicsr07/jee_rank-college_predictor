
import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("rank_model.pkl","rb"))

# Load dataset
college_df = pd.read_csv("jee_college_cutoffs_nits.csv")

st.title("JEE Rank & NIT College Predictor")

marks = st.number_input("Marks")
percentile = st.number_input("Percentile")

category = st.selectbox(
    "Category",
    ["General","OBC-NCL","SC","ST","EWS"]
)

quota = st.selectbox(
    "Quota",
    ["Other State","Home State"]
)

year = st.number_input("Year", value=2024)
candidates = st.number_input("Total Candidates", value=1200000)

if st.button("Predict Rank"):

    sample = [[marks, percentile, year, candidates]]

    rank = model.predict(sample)
    rank = int(rank[0])

    st.write("### Predicted Rank:", rank)

    possible = college_df[
        (college_df["Opening_Rank"] <= rank) &
        (college_df["Closing_Rank"] >= rank) &
        (college_df["Category"] == category) &
        (college_df["Quota"] == quota)
    ]

    st.write("### Recommended Colleges")

    st.dataframe(
        possible[["Institute","Branch","Closing_Rank"]]
        .head(10)
        .reset_index(drop=True)
    )
