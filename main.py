import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
	df = pd.read_excel(filepath, sheet_name="Sheet 1")
	pdf = FPDF(orientation="P", unit="mm", format="A4")
	pdf.add_page()
	filename = Path(filepath).stem
	invoice_num = filename.split("-")[0]
	pdf.set_font(family="Times", style="B", size=16)
	pdf.cell(w=50, h=8, txt=f"Invoice Num: {invoice_num}")
	pdf.output(f"PDFs/{filename}.pdf")





