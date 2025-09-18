from PyPDF2 import PdfReader

# Load the PDF
reader = PdfReader(r"D:\Foundation of AI\NIPS-2017-attention-is-all-you-need-Paper.pdf")

# Get metadata
info = reader.metadata
print("PDF Metadata:")
for key, value in info.items():
    print(f"{key}: {value}")

# Get number of pages
print("Number of pages:", len(reader.pages))
