# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 20:53:48 2026

@author: Grafty Mathye
"""

import streamlit as st
import pandas as pd

# Girly background styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #D63384;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# App title
st.title("💄 GlowGuide Beauty powered by Grafty")

st.write("Find makeup & skincare products that match your skin needs ")

# Load dataset
data = pd.read_csv("beauty_products.csv")

# User inputs
skin_type = st.selectbox(
    "Select your skin type:",
    ["Oily", "Dry", "Combo", "Sensitive", "All"]
)

concern = st.selectbox(
    "Select your main concern:",
    ["Acne", "Dryness", "Dark Spots", "Sensitive", "All"]
)

category = st.selectbox(
    "Choose product category:",
    ["Skincare", "Makeup"]
)

budget = st.slider(
    "Select your budget in Rands:",
    min_value=50,
    max_value=1000,
    step=10
)

# Recommendation button
if st.button("💖 Get Recommendations"):
    recommendations = data.copy()

    # Filter by category
    recommendations = recommendations[recommendations["category"] == category]

    # Price filter
    recommendations = recommendations[recommendations["price"] <= budget]

    # Simple scoring system
    recommendations["score"] = 0

    recommendations.loc[
        (recommendations["skin_type"] == skin_type) |
        (recommendations["skin_type"] == "All"),
        "score"
    ] += 1

    recommendations.loc[
        (recommendations["concern"] == concern) |
        (recommendations["concern"] == "All"),
        "score"
    ] += 1

    # Sort by score and rating
    recommendations = recommendations.sort_values(
        by=["score", "rating"],
        ascending=False
    )

    # Show top 3
    st.subheader("🌸 Top Recommendations for You")

    if recommendations.empty:
        st.write("No products found within your budget 😢")
    else:
        st.table(
            recommendations[[
                "product_name", "price", "rating"
            ]].head(3)
        )






