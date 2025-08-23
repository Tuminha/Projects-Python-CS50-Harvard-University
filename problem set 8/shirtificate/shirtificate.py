from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 50)
    pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.image("shirtificate.png", x=0, y=60, w=pdf.epw)
    pdf.set_font("helvetica", "", 24)
    pdf.cell(0, 100, f"{name} took CS50", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()