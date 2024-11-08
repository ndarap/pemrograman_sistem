import streamlit as st
import pandas as pd

st.title(":blue[Daniel Ndara Palako]")
st.write("22220044")

# Load the IoT Botnet dataset
df_botnet = pd.read_csv("/workspaces/pemrograman_sistem/UNSW_2018_IoT_Botnet_Full5pc_4.csv")

# Convert 'stime' (Unix timestamp) to datetime
df_botnet["stime"] = pd.to_datetime(df_botnet["stime"], unit='s')

# Drop rows with missing or invalid dates
df_botnet = df_botnet.dropna(subset=["stime"])

# Display the dataset columns and first few rows for verification
st.write("Dataset Columns:", df_botnet.columns)
st.write(df_botnet.head())

# Select numerical columns for analysis (e.g., 'bytes', 'pkts', 'srate', 'drate')
numerical_columns = ['pkts', 'bytes', 'srate', 'drate']

# Create a pivot table with 'stime' as index and aggregate the numerical columns
df_botnet_analysis = df_botnet.pivot_table(index='stime', values=numerical_columns, aggfunc='sum')

# Display the area chart
st.title("Area Chart")
st.area_chart(df_botnet_analysis)

st.markdown("---")

# Display the bar chart
st.title("Bar Chart")
st.bar_chart(df_botnet_analysis)

st.markdown("---")

# Display the line chart
st.title("Bar Chart")
st.bar_chart(df_botnet_analysis)
