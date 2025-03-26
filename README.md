# Financial Chatbot

## Overview
This chatbot allows users to retrieve financial information (e.g., revenue, net income, assets) for Microsoft, Tesla, and Apple based on their 10-K filings. 

## How It Works
1. The chatbot reads financial data from a CSV file (`Finance_data.csv`).
2. Users can enter a **company name**, a **year**, and select from predefined **financial queries**.
3. The chatbot filters the dataset and provides an appropriate response.
4. If the requested data is missing, it informs the user accordingly.

## Predefined Queries
- What is the total revenue?
- How has net income changed over the last year?
- What are the total assets?
- What are the total liabilities?
- What is the cash flow from operating activities?

## How to Run
1. Install dependencies:
   ```bash
   pip install pandas

Limitations!!!
Can only answer predefined financial questions.

Works only with Microsoft, Tesla, and Apple.

Requires a properly formatted CSV file.

Future Improvements!!!
Use Natural Language Processing (NLP) for more flexible queries.

Fetch real-time financial data from APIs.

Convert to a web-based chatbot using Flask or Streamlit.

# Forage_GenAI
