from app.ingest.pdf_loader import extract_pdf_text

pages = extract_pdf_text("sample.pdf") # use a real report

print(f"Total pages extracted: {len(pages)}\n")
print("Preview of page 1:\n")
print(pages[0]["text"][:1000])