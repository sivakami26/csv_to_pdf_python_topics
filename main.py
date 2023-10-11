from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", format="A4", unit="mm")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align = "L", border=1, ln=1)
    pdf.line(10,21,200, 21)
    for iterator in range(1, row["Pages"]):
        pdf.add_page()
pdf.output("output.pdf")



