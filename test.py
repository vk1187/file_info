import os
import csv

BASE_DIR = "/home/vivek/Desktop/inte/hostel"
OUTPUT_CSV = "pdf_basic_info.csv"

def find_pdfs_basic(root_folder):
    pdf_list = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith(".pdf"):
                full_path = os.path.abspath(os.path.join(root, file))
                parent_folder = os.path.basename(os.path.dirname(full_path))
                pdf_list.append({
                    "file_name": file,
                    "full_path": full_path,
                    "parent_folder": parent_folder
                })
    return pdf_list

def save_to_csv(pdf_list, csv_path):
    if not pdf_list:
        print("No PDF files found.")
        return

    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=pdf_list[0].keys())
        writer.writeheader()
        for row in pdf_list:
            writer.writerow(row)

    print(f"✅ Basic PDF info saved to: {csv_path}")

if __name__ == "__main__":
    data = find_pdfs_basic(BASE_DIR)
    save_to_csv(data, OUTPUT_CSV)
