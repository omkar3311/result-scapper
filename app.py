import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Shivaji University Results", layout="wide")

st.title("🎓 Shivaji University Result Dashboard")

csv_file = "result.csv"

if not os.path.exists(csv_file):
    st.error("result.csv not found in current directory")
    st.stop()

df = pd.read_csv(csv_file)
ranked_df = df.sort_values(by="percentage", ascending=False).reset_index(drop=True)
ranked_df.index += 1
ranked_df.insert(0, "Rank", ranked_df.index)


col1, col2 = st.columns([1, 2])

with col1:
    butt = st.button("🏆 Show Full Ranking")
if butt:
    st.subheader("🏆 Ranked Results (High → Low Percentage)")
    st.dataframe(ranked_df, use_container_width=True)
with col2:
    search_name = st.text_input("🔍 Search your name to see rank")

    if search_name:
        matches = ranked_df[
            ranked_df["name"].str.contains(search_name, case=False, na=False)
        ]

        if not matches.empty:
            st.subheader("🎯 Search Result")
            st.dataframe(matches, use_container_width=True)
        else:
            st.warning("No matching name found")
st.divider()

st.subheader("📄 Results (Original Order)")
st.dataframe(df, use_container_width=True)


