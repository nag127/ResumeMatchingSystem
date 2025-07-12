from config import llm

def summarize_and_score(info, job_description):
    prompt = f"""
    Given the following extracted resume info and the job description, rate the candidate from 1 to 10 in terms of relevance. Also provide a brief summary of why this person is a good or bad match.

    Resume Info:
    {info}

    Job Description:
    {job_description}

    Respond in this format:
    - Name:
    - Relevance Score (only number like 7):
    - Summary:
    """
    response = llm.invoke(prompt)
    return response.content  # ✅ Return only the string content
