from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", format="A4", unit="mm")
pdf.set_auto_page_break(auto=False, margin=0)
for index, row in df.iterrows():
    # Add master page
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", border=0, ln=0)

    for y in range(20, 278, 10):
        pdf.line(10, y, 200, y)

    # Set the footer for master page
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", border=0, ln=0)

    for iterator in range(row["Pages"] - 1):
        pdf.add_page()
        for y in range(20, 288, 10):
            pdf.line(10, y, 200, y)
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", border=0, ln=0)

pdf.output("output.pdf")
