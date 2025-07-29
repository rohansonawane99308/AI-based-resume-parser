import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    with fitz.open(file_path) as doc:
        return " ".join(page.get_text() for page in doc)

def extract_skills(text):
    skills = ['python', 'sql', 'excel', 'power bi', 'machine learning', 'data analysis',
              'communication', 'management', 'keras', 'tensorflow', 'pytorch']
    return list({skill for skill in skills if skill.lower() in text.lower()})