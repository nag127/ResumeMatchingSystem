from config import llm

def extract_resume_info(resume_text):
    prompt = f"""
    Extract the following information from this resume:
    - Full Name
    - Designation
    - Years of Experience
    - Location
    - Email ID
    - Mobile Number
    - LinkedIn URL
    - Achievements
    - Awards
    - Certifications
    - Technical Skills
    - Domain Expertise

    Resume:
    {resume_text}
    """
    response = llm.invoke(prompt)
    return response.content  # ✅ Return only the string content
