def extract_content_from_pdf(file_path):
    # Function to extract content from a PDF file
    import PyPDF2
    content = ""
    
    with open(file_path, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        for page_num in range(pdf.getNumPages()):
            page = pdf.getPage(page_num)
            content += page.extractText()
    
    return content
