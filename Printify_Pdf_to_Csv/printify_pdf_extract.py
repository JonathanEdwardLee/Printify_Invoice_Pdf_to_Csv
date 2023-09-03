import pdfplumber

def extract_table_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_data = []

        for page in pdf.pages:
            table = page.extract_table()
            if table:
                all_data.extend(table)

    # Print the first 10 rows to inspect
    for row in all_data[:10]:
        print(row)

    # Commented out DataFrame creation for inspection purposes
    # df = pd.DataFrame(all_data[1:], columns=all_data[0])
    return all_data  # Returning raw data for now

if __name__ == "__main__":
    pdf_path = "C:\\Users\\your\\path\\here.pdf"
    data = extract_table_from_pdf(pdf_path)
    # Commented out other operations for inspection purposes
