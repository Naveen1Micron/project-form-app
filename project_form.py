import streamlit as st
from datetime import date

# Title of the app
st.title("Project Input Form")

# Input fields
project_name = st.text_input("Enter the project name")
client_name = st.text_input("Enter the client name")
budget = st.number_input("Enter the budget (INR)", min_value=0)
deadline = st.date_input("Enter the deadline", min_value=date.today())
project_type = st.selectbox("Select the project type", ["Web", "Mobile", "AI", "Other"])
description = st.text_area("Enter the project description")

# Submit button
if st.button("Submit"):
    # Display the summary
    st.success("Here is your project summary:")
    st.write(f"**Project Name:** {project_name}")
    st.write(f"**Client Name:** {client_name}")
    st.write(f"**Budget:** ₹{budget}")
    st.write(f"**Deadline:** {deadline}")
    st.write(f"**Project Type:** {project_type}")
    st.write(f"**Description:** {description}")
