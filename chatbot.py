import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Columns in dataset:", df.columns.tolist())
        return df
    except Exception as e:
        print("Error loading data:", e)
        return None

def get_financial_data(df, company, year, query):
    try:
        year = int(year)
        company = company.strip()
        
        if "Company" not in df.columns or "year" not in df.columns:
            print("Error: Required columns not found in CSV.")
            return "Data format issue."
        
        result = df[(df['Company'].str.lower() == company.lower()) & (df['year'] == year)]
        
        if result.empty:
            return "No data found for the given company and year."
        
        query_mapping = {
            "What is the total revenue?": "Total Revenue",
            "How has net income changed over the last year?": "Net Income",
            "What are the total assets?": "Total Assets",
            "What are the total liabilities?": "Total Liabilities",
            "What is the cash flow from operating activities?": "Cash Flow from Operating Activities"
        }
        
        column_name = query_mapping.get(query)
        
        if column_name:
            return f"{query} {result.iloc[0][column_name]}"
        else:
            return "Sorry, I can only provide information on predefined queries."
    except Exception as e:
        return f"Error: {str(e)}"

def chatbot():
    file_path = "D:\Downloads\Finance_data.csv"  # Path to uploaded CSV
    df = load_data(file_path)
    
    if df is None:
        return
    
    print("\nWelcome to the Financial Chatbot! Type 'exit' to quit.")
    
    while True:
        company = input("Enter the company name: ")
        if company.lower() == 'exit':
            break
        
        year = input("Enter the year (e.g., 2023): ")
        if year.lower() == 'exit':
            break
        
        print("Available queries:")
        queries = [
            "What is the total revenue?",
            "How has net income changed over the last year?",
            "What are the total assets?",
            "What are the total liabilities?",
            "What is the cash flow from operating activities?"
        ]
        for i, q in enumerate(queries, 1):
            print(f"{i}. {q}")
        
        query = input("Enter your query: ")
        if query.lower() == 'exit':
            break
        
        response = get_financial_data(df, company, year, query)
        print(response)

if __name__ == "__main__":
    chatbot()
