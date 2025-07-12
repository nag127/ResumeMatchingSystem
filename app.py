from flask import Flask, request, render_template
import os
import markdown
from agents.resume_reader import read_resumes
from agents.info_extractor import extract_resume_info
from agents.relevance_ranker import summarize_and_score
from agents.markdown_report import generate_markdown

app = Flask(__name__)

# Helper to convert Markdown to HTML
def read_markdown_as_html_from_string(markdown_text):
    return markdown.markdown(markdown_text, extensions=["tables", "fenced_code"])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job_description = request.form['job_description']
        resume_folder = request.form['resume_folder']

        # Step 1: Read resumes as text
        resume_texts = read_resumes(resume_folder)

        # Step 2: Extract info from each resume
        extracted_infos_raw = [extract_resume_info(text) for text in resume_texts]

        # Optional: Convert extracted info dicts to Markdown strings
       

        # Step 3: Get LLM-based scoring + summary
        summaries_raw = [summarize_and_score(info, job_description) for info in extracted_infos_raw]
       # summaries_html = [read_markdown_as_html_from_string(summary) for summary in summaries_raw]

        # Step 4: Convert final summary to Markdown and HTML
        markdown_output = generate_markdown(summaries_raw)
        html_output = read_markdown_as_html_from_string(markdown_output)

        return render_template('index.html',
                               output_html=html_output,
                               extracted_infos=extracted_infos_raw,
                               job_description=job_description)

    return render_template('index.html', output_html=None, extracted_infos_html=None, summaries_html=None, job_description="")

if __name__ == '__main__':
    app.run(debug=True)
