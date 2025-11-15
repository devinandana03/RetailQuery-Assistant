# app.py
import streamlit as st
import re
import os
import ast
import pandas as pd
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

# -----------------------------
# Load Environment
# -----------------------------
load_dotenv()

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="RetailQuery Assistant", layout="centered")
st.title("RetailQuery Assistant")

# -----------------------------
# Load LLM + DB (Cached)
# -----------------------------
@st.cache_resource(show_spinner="Connecting to database and AI model…")
def load_chain():
    llm = GoogleGenerativeAI(
        model="gemini-2.5-flash",               
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0
    )
    db = SQLDatabase.from_uri(
        "mysql+pymysql://root:root123@localhost/retail_db",
        sample_rows_in_table_info=3
    )
    chain = SQLDatabaseChain.from_llm(
        llm=llm,
        db=db,
        verbose=False,
        return_intermediate_steps=True
    )
    return chain, db

chain, db = load_chain()

# -----------------------------
# Robust SQL Extractor
# -----------------------------
def clean_sql(text: str) -> str | None:
    """Extract only valid SELECT …; queries. Ignore explanations."""
    if not text:
        return None
    text = re.sub(r"```[\w]*", "", text)
    text = re.sub(r"```", "", text)
    match = re.search(r"\bSELECT\b[\s\S]*?;", text, re.IGNORECASE)
    if match:
        sql = match.group(0).strip()
        if sql.upper().startswith("SELECT"):
            return sql
    return None

# -----------------------------
# UI
# -----------------------------
with st.container():
    question = st.text_input(
        "Enter your question:",
        placeholder="How many customers are there?",
        key="question_input",
        label_visibility="collapsed"
    )

    col1, col2 = st.columns([1, 4])
    with col1:
        execute = st.button("Execute", type="primary", use_container_width=True)
    with col2:
        st.caption("Press Enter to apply")

# Tip
st.caption("Tip: Ask about sales, revenue, categories, or customer spending from the retail_sales table.")

# -----------------------------
# Process Query (Safe & Clean)
# -----------------------------
if execute and question.strip():
    with st.spinner("Thinking…"):
        try:
            # 1. Run LangChain
            result = chain.invoke({"query": question})
            llm_output = result["result"]

            # 2. Extract SQL only if valid
            sql = clean_sql(llm_output)
            raw_result = None

            # 3. Execute only valid SELECT queries
            if sql and sql.strip().upper().startswith("SELECT"):
                try:
                    raw_result = db.run(sql)
                except Exception as e:
                    st.error(f"SQL Execution Failed: {e}")
                    st.code(sql, language="sql")

            # 4. Clean answer text
            answer = llm_output.strip()
            answer = re.sub(r"```[\w]*|```", "", answer)                # remove code fences
            answer = re.sub(r"^(Answer|SQLResult)[:\s]*", "", answer, flags=re.IGNORECASE)
            answer = re.sub(r"SQLResult[:\s].*", "", answer, flags=re.IGNORECASE).strip()

            # 5. Show Answer
            st.markdown("### Answer")
            st.success(answer)

            # 6. Show Table (only if real data exists)
            if raw_result and raw_result.strip():
                try:
                    data = ast.literal_eval(raw_result) if isinstance(raw_result, str) else raw_result
                    if data and isinstance(data, (list, tuple)):
                        if isinstance(data[0], (list, tuple)) and len(data[0]) > 1:
                            # Multi-column table
                            df = pd.DataFrame(data)
                            st.markdown("**Result Table:**")
                            st.dataframe(df, use_container_width=True)
                        else:
                            # Single-value list
                            flat = [row[0] if isinstance(row, (list, tuple)) else row for row in data]
                            st.markdown("**Result:**")
                            st.write(flat)
                except Exception:
    
                    pass


        except Exception as e:
            st.error(f"Unexpected error: {e}")

elif execute:
    st.info("Please enter a question first.")