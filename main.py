import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

	pdf = FPDF(orientation="P", unit="mm", format="A4")
	pdf.add_page()

	filename = Path(filepath).stem
	invoice_num, invoice_date = filename.split("-")

	pdf.set_font(family="Times", style="B", size=16)
	pdf.cell(w=50, h=8, txt=f"Invoice Num: {invoice_num}", ln=1)

	pdf.set_font(family="Times", style="B", size=16)
	pdf.cell(w=50, h=8, txt=f"Date: {invoice_date}", ln=1)

	df = pd.read_excel(filepath, sheet_name="Sheet 1")
	columns = list(df.columns)
	columns = [item.replace("_", " ").title() for item in columns]

	# Add Header
	pdf.set_font(family="Times", size=10, style="B")
	pdf.set_text_color(80, 80, 80)
	pdf.cell(w=30, h=8, txt=str(columns[0]), border=1)
	pdf.cell(w=60, h=8, txt=str(columns[1]), border=1)
	pdf.cell(w=40, h=8, txt=str(columns[2]), border=1)
	pdf.cell(w=30, h=8, txt=str(columns[3]), border=1)
	pdf.cell(w=30, h=8, txt=str(columns[4]), border=1, ln=1)

	# Add rows to the table
	for index, row in df.iterrows():
		pdf.set_font(family="Times", size=10)
		pdf.set_text_color(80, 80, 80)
		pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
		pdf.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
		pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
		pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
		pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

	# Add total sum
	total_sum = df["total_price"].sum()
	pdf.set_font(family="Times", size=10)
	pdf.set_text_color(80, 80, 80)
	pdf.cell(w=30, h=8, txt="", border=1)
	pdf.cell(w=60, h=8, txt="", border=1)
	pdf.cell(w=40, h=8, txt="", border=1)
	pdf.cell(w=30, h=8, txt="", border=1)
	pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

	# Add total sum sentence
	pdf.set_font(family="Times", size=10, style="B")
	pdf.cell(w=30, h=8, txt=f"The total price is {total_sum}", ln=1)

	# Add author name and logo
	pdf.set_font(family="Times", size=10, style="B")
	pdf.cell(w=20, h=8, txt=f"Created by HOUZH")
	pdf.image("pythonhow.png", x=42, w=8)






	pdf.output(f"PDFs/{filename}.pdf")





