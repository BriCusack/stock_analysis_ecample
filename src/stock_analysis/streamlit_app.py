import streamlit as st
import os

from stock_analysis.main import st_run

st.title('LOCAL RESTAURANT FINDER')
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["SERPER_API_KEY"] = st.secrets["SERPER_API_KEY"]

with st.sidebar:
    st.header('Enter Research Details')
    company_code = st.text_input("Enter a company code:")


if st.button('Run Research'):
    if not company_code:
        st.error("Please fill all the fields.")
    else:
        inputs = {
            "company_code": str(company_code)
        }
        research_crew = st_run(inputs)
        st.subheader("Results of your research project:")
        with open('report.md', 'r') as file:
            st.write(file.read())