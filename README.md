# 🤖 AI-Powered Data Cleaning & Preprocessing App

### 🚀 Automated Data Cleaning with AI-Driven Suggestions

---

## 📌 Overview

The **AI-Powered Data Cleaning App** is a Streamlit-based web application that automates the process of cleaning and preprocessing CSV and Excel datasets.

It combines:

* ⚙️ Rule-based data cleaning pipeline
* 🤖 AI-powered suggestions using a local LLM (Llama3 via Ollama)

This helps transform **raw, messy datasets into clean, analysis-ready data** with minimal manual effort.

---

## ✨ Key Features

* 📂 Upload CSV or Excel files directly
* 🧹 Automatic duplicate removal
* 🏷️ Column name standardization
* ❗ Smart missing value handling
* 🔤 Text cleaning (lowercase + whitespace removal)
* 📧 Email validation and invalid flagging
* 📅 Automatic date/time detection
* 📊 Outlier removal using IQR method
* 🤖 AI-driven preprocessing suggestions
* ⬇️ Download cleaned dataset

---

## 🏗️ Project Structure

```
AI_Data_Cleaning_App/
│
├── app.py                # Streamlit UI & workflow
├── data_cleaning.py      # DataCleaning class (core logic)
├── ai_module.py          # AI integration (Ollama API)
├── requirements.txt      # Dependencies
├── sample_data.csv       # Sample dataset
├── Book1.xlsx            # Sample dataset
└── README.md             # Project documentation
```

---

## ⚙️ Tech Stack

* **Frontend/UI:** Streamlit
* **Data Processing:** Pandas, NumPy
* **AI Integration:** Ollama (Llama3)
* **File Handling:** OpenPyXL
* **API Calls:** Requests

---

## 📦 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI_Data_Cleaning_App.git
cd AI_Data_Cleaning_App
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Setup Ollama (Local AI)

1. Install Ollama: https://ollama.com
2. Pull model:

```bash
ollama pull llama3
```

3. Start Ollama:

```bash
ollama serve
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

👉 Open in browser:
http://localhost:8501

---

## 🔄 Data Cleaning Pipeline

| Step | Action                | Description                   |
| ---- | --------------------- | ----------------------------- |
| 1    | Remove Duplicates     | Drops duplicate rows          |
| 2    | Standardize Columns   | Lowercase + clean names       |
| 3    | Handle Invalid Values | Convert null-like values      |
| 4    | Convert Data Types    | Safe numeric conversion       |
| 5    | Missing Values        | Median (numeric), Mode (text) |
| 6    | Text Cleaning         | Strip + lowercase             |
| 7    | Email Validation      | Regex-based validation        |
| 8    | Date Conversion       | Auto-detect date columns      |
| 9    | Outlier Removal       | IQR method                    |
| 10   | Reset Index           | Clean final dataset           |

---

## 🤖 AI Module

The AI module:

* Sends data to **Llama3 via Ollama API**
* Uses:

```
http://localhost:11434/api/generate
```

* Returns:

  * Data preprocessing suggestions
  * Insights on dataset quality

---

## 📊 How to Use

1. Upload `.csv` or `.xlsx` file
2. View **Original Data**
3. See **Cleaned Data**
4. Check **AI Suggestions**
5. Download cleaned dataset

---

## ⚠️ Limitations

* Requires **Ollama running locally**
* Large datasets may be slow
* Date detection is heuristic-based
* Email validation may not cover all edge cases
* Outlier removal may reduce dataset size significantly

---

## 🎯 Use Cases

* Data Analyst Projects
* Data Cleaning Automation
* Preprocessing before Machine Learning
* Exploratory Data Analysis (EDA)

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Naman Gupta**
📊 Aspiring Data Analyst

---

## ⭐ Final Note

This project demonstrates:

* Real-world data cleaning pipeline
* AI integration in analytics workflow
* End-to-end project (UI + Backend + AI)
