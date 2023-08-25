import pdfplumber
import re
import pandas as pd

def extract_table_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_text = ""
        for page in pdf.pages:
            all_text += page.extract_text()

        # Specific regex pattern with the re.DOTALL flag
        pattern = r"Net Amount Total.*?\(excl tax\)\s*USD ([\d.]+)\s*USD ([\d.]+)\s*USD ([\d.]+)\s*USD ([\d.]+)"

        matches = re.search(pattern, all_text, re.DOTALL)

        if matches:
            net_amount = matches.group(1)
            shipping_cost = matches.group(2)
            tax = matches.group(3)
            total_invoice_amount = matches.group(4)
        else:
            net_amount, shipping_cost, tax, total_invoice_amount = "Not Matched", "Not Matched", "Not Matched", "Not Matched"

        print("Net Amount Total (excl tax):", net_amount)
        print("Shipping cost:", shipping_cost)
        print("Tax:", tax)
        print("Total invoice amount:", total_invoice_amount)

        # Create DataFrame and save
        df = pd.DataFrame({
            "Net Amount Total (excl tax)": [net_amount],
            "Shipping cost": [shipping_cost],
            "Tax": [tax],
            "Total invoice amount": [total_invoice_amount]
        })
        
        return df

if __name__ == "__main__":
    pdf_path = "C:\\Users\\your\\path\\here.pdf"
    df = extract_table_from_pdf(pdf_path)
    df.to_csv('YourFileNameHere.csv', index=False)
