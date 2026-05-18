import sys
from fpdf import FPDF
try:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(0, 10, "Title", new_x="LMARGIN", new_y="NEXT", align='C')
    
    pdf.set_font('helvetica', 'B', 9)
    pdf.cell(0, 6, "1. CVE-2023-1234 (CRITICAL)", new_x="LMARGIN", new_y="NEXT")
    
    print("X before multi_cell 1:", pdf.get_x())
    pdf.set_font('helvetica', '', 8)
    pdf.multi_cell(0, 4, "Package: openssl (1.0.0)", new_x="LMARGIN", new_y="NEXT")
    
    print("X before multi_cell 2:", pdf.get_x())
    pdf.multi_cell(0, 4, "Title: Buffer overflow in openssl", new_x="LMARGIN", new_y="NEXT")
    print("Success!")
except Exception as e:
    print(f"Error: {e}")
