import pdfkit

def htmlToPDF(html, filename):
    pdfkit.from_string(html, f"pdfs/{filename}")
    return True