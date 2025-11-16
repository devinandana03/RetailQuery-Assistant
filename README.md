# RetailQuery Assistant  
**AI-Powered Retail Database Querying Tool**

RetailQuery Assistant is an intelligent natural-language interface that allows users to query a MySQL retail sales database **without writing SQL**.  
Built using **Streamlit**, **LangChain**, and **Google Gemini**, this app translates everyday questions into accurate database insights and presents them in clean, easy-to-understand responses.

---
![image_alt](https://github.com/devinandana03/RetailQuery-Assistant/blob/master/ss_chatbot.png?raw=true)
---

## Features
- Ask questions in **plain English** — no SQL required  
- AI-powered query generation using **Google Gemini**  
- Automatic SQL extraction & **safe execution**  
- Clean natural-language answers  
- User-friendly **Streamlit UI**

---

## Database Information
The app connects to a MySQL database: **`retail_db`**  

It uses a central table: **`retail_sales`**

| Column Name      | Description                                   |
|------------------|-----------------------------------------------|
| `transaction_id` | Unique ID for every sale                      |
| `customer_id`    | ID of customer making the purchase            |
| `gender`         | Customer gender                               |
| `age`            | Customer age                                  |
| `category`       | Product category (Electronics, Beauty, Clothing) |
| `quantity`       | Units purchased                               |
| `price`          | Price per unit                                |
| `total_amount`   | Final bill amount                             |
| `date`           | Date of transaction                           |

---

## Tech Stack
- **Python**  
- **Streamlit**  
- **LangChain**  
- **Google Generative AI (Gemini)**  
- **MySQL + PyMySQL**  
- **Pandas**

---

## Local Setup
```bash
# 1. Clone the repo
git clone https://github.com/devinandana03/RetailQuery-Assistant.git
cd RetailQuery-Assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
