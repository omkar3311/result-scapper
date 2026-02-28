# 🎓 Shivaji University Result Scraper & Dashboard

This project automates the process of **fetching Shivaji University results**, extracting marks from official PDF mark sheets, storing them in a CSV file, and visualizing them through an interactive **Streamlit dashboard** with ranking and search functionality.

---

## 📌 Features

- Fetches **official marksheets (PDF)** directly from the Shivaji University result API
- Extracts:
  - Student name
  - PRN
  - Subject-wise final marks (obtained / max)
  - Total marks
  - Percentage
- Stores results in a structured `result.csv`
- Streamlit dashboard to:
  - View results in table format
  - Rank students by percentage
  - Search a student by name and see their rank

---

## 📂 Project Structure
```bash
├── fetch.py # Fetches results and generates result.csv
├── app.py # Streamlit dashboard
├── result.csv # Generated results (created automatically)
├── README.md # Project documentation
```

---

## ⚙️ Requirements

Python 3.9+

Install dependencies:

```bash
pip install requests pdfplumber streamlit pandas
```

🚀 Step 1: Fetch Results (fetch.py)
🔧 Configuration

Edit the PRNS dictionary in fetch.py:
```bash
PRNS = {
    # prn : name (name is only for reference)
    12345667: "Student Name"
}
```
## 👨‍💻 **Author**

   **Omkar Waghmare**  
🎓 Aspiring Data Scientist.
