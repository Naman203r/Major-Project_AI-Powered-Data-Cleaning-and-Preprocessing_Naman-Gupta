# Major-Project_AI-Powered-Data-Cleaning-and-Preprocessing_Naman-Gupta

🤖 AI-Powered Data Cleaning App
Automated Data Cleaning with AI-Driven Suggestions

Overview
The AI-Powered Data Cleaning App is a Streamlit-based web application that automates the process of cleaning and preprocessing CSV and Excel datasets. It uses a universal DataCleaning engine to standardize, fix, and transform raw data, then leverages a local LLM (via Ollama) to provide intelligent AI suggestions for further preprocessing steps.

Features
•	Upload CSV or Excel files directly via the web interface
•	Automatic duplicate removal and column name standardization
•	Smart handling of missing values (median for numbers, mode for text)
•	Text column cleaning: strip whitespace, lowercase normalization
•	Email address validation and flagging of invalid entries
•	Intelligent date/time column detection and conversion
•	Outlier removal using the IQR (Interquartile Range) method
•	AI-generated suggestions via a local Llama3 model (Ollama)
•	Download cleaned data as a CSV file

Project Structure
The project consists of three main Python files and supporting assets:

File	Description
app.py	Main Streamlit application — handles file upload, UI rendering, and orchestrates cleaning and AI suggestions
data_cleaning.py	DataCleaning class with a universal clean_data() method that applies all cleaning steps
ai_module.py	ask_ai() function that sends prompts to the local Llama3 model via Ollama API
requirements.txt	Python package dependencies for the project
Book1.xlsx / sample_data.csv	Sample datasets for testing the application

Prerequisites
Python Requirements
Install the required Python packages using pip:
pip install -r requirements.txt

The key Python dependencies include:
•	streamlit — Web application framework
•	pandas — Data manipulation and analysis
•	numpy — Numerical computing
•	openpyxl — Excel file support
•	requests — HTTP calls to the Ollama API

Ollama (Local AI)
The app uses Ollama to run the Llama3 model locally. To set it up:
1.	Download and install Ollama from https://ollama.com
2.	Pull the Llama3 model:
ollama pull llama3
3.	Ensure Ollama is running on http://localhost:11434 before launching the app.

Installation & Usage
1. Clone the Repository
git clone https://github.com/your-username/AI_Data_Cleaning_App.git
cd AI_Data_Cleaning_App

2. Install Dependencies
pip install -r requirements.txt

3. Start Ollama
ollama serve

4. Run the App
streamlit run app.py
The app will open in your browser at http://localhost:8501

Data Cleaning Pipeline
The DataCleaning class applies the following steps in sequence to any uploaded dataset:

Step	Action	Details
1	Remove Duplicates	Drops all fully duplicate rows
2	Standardize Columns	Lowercases, strips, replaces spaces/hyphens with underscores
3	Replace Invalid Values	Converts empty strings, 'nan', 'null', 'none' to NaN
4	Convert Numeric Columns	Safely coerces strings to numeric types where possible
5	Handle Missing Values	Fills numeric NaN with median; text NaN with mode or 'unknown'
6	Clean Text Columns	Strips whitespace and lowercases all string values
7	Validate Emails	Validates email columns with regex; flags invalid as 'invalid_email'
8	Convert Dates	Auto-detects date/time columns by name and parses them
9	Remove Outliers	Applies IQR method (1.5x) to numeric columns with >5 unique values
10	Reset Index	Resets DataFrame index after all transformations

AI Module
The ai_module.py file provides a single function ask_ai(prompt) that:
•	Sends a POST request to the local Ollama API endpoint at http://localhost:11434/api/generate
•	Uses the llama3 model in non-streaming mode
•	Returns the AI's text response or an error message if the call fails

The app constructs a prompt containing the cleaned dataframe's column names and the first 10 rows of data, then displays the AI's preprocessing suggestions in the Streamlit UI.

How to Use
4.	Open the app at http://localhost:8501 in your browser.
5.	Click "Upload File" and select a .csv or .xlsx file.
6.	The original dataset and its shape are displayed in the "Original Data" section.
7.	The cleaned dataset is shown in the "Cleaned Data" section with its updated shape.
8.	AI suggestions are generated and displayed in the "AI Suggestions" section.
9.	Click "Download Cleaned CSV" to save the cleaned file to your machine.

Notes & Limitations
•	The app requires Ollama to be running locally; if it is offline, AI suggestions will show an error message.
•	The outlier removal step may reduce row count significantly for datasets with extreme values.
•	Date parsing is heuristic — columns are only converted if their name contains 'date' or 'time'.
•	Email validation uses a regex pattern; complex or unusual email formats may be incorrectly flagged.
•	The app processes data entirely in-memory; very large files may be slow depending on system resources.

License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it with attribution.


Built with Streamlit • Pandas • Ollama • Llama3
