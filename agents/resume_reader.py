import os
from utils.file_loader import load_file_text

def read_resumes(folder_path):
    resume_texts = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf') or filename.endswith('.docx'):
            filepath = os.path.join(folder_path, filename)
            resume_texts.append(load_file_text(filepath))
    return resume_texts