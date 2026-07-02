import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="EDA App", page_icon="📊")
st.title("Streamlit App - EDA_App")

st.write("This app shows a simple exploratory data analysis using sample data.")

# Sample dataset
sample_data = pd.DataFrame({
    "Category": ["A", "B", "C", "D", "E"],
    "Value": [10, 25, 15, 30, 20]
})

st.subheader("Dataset")
st.dataframe(sample_data)

st.subheader("Bar Chart")
fig, ax = plt.subplots()
ax.bar(sample_data["Category"], sample_data["Value"], color="skyblue")
ax.set_title("Sample Values by Category")
ax.set_ylabel("Value")
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("Summary")
st.metric("Total", sample_data["Value"].sum())
st.metric("Average", round(sample_data["Value"].mean(), 2))

