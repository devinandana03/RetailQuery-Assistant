🛒RetailQuery Assistant
AI-Powered Retail Database Querying Tool

RetailQuery Assistant is an intelligent natural-language interface that allows users to query a MySQL retail sales database without writing SQL.
Built using Streamlit, LangChain, and Google Gemini, this app translates everyday questions into accurate database insights and presents them in clean, easy-to-understand responses.
___________________________________________________________________________________________________________________________________________________________________________________________
#Features
*Ask questions in plain English — no SQL required
*AI-powered query generation using Google Gemini
*Automatic SQL extraction & safe execution
*Clean natural-language answers
*User-friendly Streamlit UI

___________________________________________________________________________________________________________________________________________________________________________________________

# Database Information

The app connects to a MySQL database: retail_db
It uses a central table:

#retail_sales
*Column Name:	Description
*transaction_id:	Unique ID for every sale
*customer_id:	ID of customer making the purchase
*gender:	Customer gender
*age:	Customer age
*category:	Product category (Electronics, Beauty, Clothing)
*quantity:	Units purchased
*price:	Price per unit
*total_amount:	Final bill amount
*date:	Date of transaction

___________________________________________________________________________________________________________________________________________________________________________________________
# Tech Stack

*Python
*Streamlit
*LangChain
*Google Generative AI 
*MySQL + PyMySQL
*Pandas
___________________________________________________________________________________________________________________________________________________________________________________________
