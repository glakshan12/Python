import pdfkit

# HTML file path
html_file = 'resume.html'

# Output PDF file path
pdf_file = 'LakshanG_Resume.pdf'

# Convert HTML to PDF
pdfkit.from_file(html_file, pdf_file)
