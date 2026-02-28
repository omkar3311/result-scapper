import requests
import pdfplumber
import re
import csv
import os
from io import BytesIO

PRNS = {
    #prn     :  name
    12345667 : "name"
    
}

url = "https://sukapps.unishivaji.ac.in/exam_pro_api/api/MarksheetController/RPT_ONLINEMARKSSTATEMENT"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Origin": "https://sukapps.unishivaji.ac.in",
    "Referer": "https://sukapps.unishivaji.ac.in/exam-app/",
    "User-Agent": "Mozilla/5.0"
}

rows = []
all_subjects = set()
i = 1
for prn, name_expected in PRNS.items():
    res = requests.post(url, json={"PRN": str(prn)}, headers=headers)

    text = ""
    with pdfplumber.open(BytesIO(res.content)) as pdf:
        for p in pdf.pages:
            t = p.extract_text()
            if t:
                text += t + "\n"

    name = re.search(r"Name\s*:\s*(.+?)\s+Seat", text).group(1)

    blocks = re.split(r"\n(?=\d{5}\s)", text)

    subject_data = {}
    total_obtained = 0
    total_max = 0

    for block in blocks:
        header = re.match(r"\d{5}\s+(.+?)\s", block)
        if not header:
            continue

        subject = header.group(1).strip().split()[0]

        final_match = re.search(r"PASS\s+(\d{2,3})\s+PASS", block)
        if not final_match:
            continue

        obtained = int(final_match.group(1))
        max_marks = sum(int(x) for x in re.findall(r"\((\d{2,3})\)", block))

        subject_data[subject] = f"{obtained}/{max_marks}"
        total_obtained += obtained
        total_max += max_marks
        all_subjects.add(subject)

    percentage = round((total_obtained / total_max) * 100, 2)

    row = {
        "name": name,
        "prn": prn,
        **subject_data,
        "total": f"{total_obtained}/{total_max}",
        "percentage": percentage
    }

    rows.append(row)
    print(i)
    i = i+1

csv_file = "result.csv"
subjects_sorted = sorted(all_subjects)
fieldnames = ["name", "prn"] + subjects_sorted + ["total", "percentage"]

file_exists = os.path.exists(csv_file)

with open(csv_file, "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    if not file_exists:
        writer.writeheader()
    for r in rows:
        writer.writerow(r)

print("✅ result.csv updated successfully")