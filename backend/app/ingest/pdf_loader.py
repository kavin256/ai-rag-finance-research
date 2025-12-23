from pypdf import PdfReader

def extract_pdf_text(file_path: str) -> list[dict]:
    
    """
    Extract text from a pdf file page by page.

    Returns:
        A list of dictionaries with:
            - page_number (1-based)
            - text content
    """
    
    reader = PdfReader(file_path)
    extracted_pages = []

    for index, page in enumerate(reader.pages):
        text = page.extract_text()

        if not text:
            continue

        extracted_pages.append({
            "page_number":index + 1,
            "text": text.strip()
        })

    return extracted_pages