```markdown
# Resume Matching System

## Description

The Resume Matching System is a web application designed to efficiently match candidate resumes against job descriptions to evaluate relevance and suitability. This system leverages the Flask web framework and language models for natural language processing tasks, providing a streamlined solution for HR professionals and hiring managers to automate and enhance the resume screening process.

## Features

- **Resume Reading and Parsing**: Supports PDF and DOCX formats using `PyPDF2` and `docx2txt` libraries to extract raw text.
- **Information Extraction**: Utilizes a Large Language Model (LLM) to extract detailed candidate information from resumes.
- **Relevance Scoring and Summary**: Compares resume data with job descriptions to generate relevance scores and summarizations.
- **Markdown and HTML Report Generation**: Formats the results into markdown and converts them to HTML for presentation.
- **User Interface**: Offers a simple HTML form for job description input and resume folder path specification, displaying processed results on a web interface.

## Prerequisites

- Python 3.x
- Git (if cloning the repository)
- OpenAI API Key

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YourUsername/ResumeMatching.git
   cd ResumeMatching
   ```

2. **Install Python and Pip**
   - Install Python from [python.org](https://www.python.org/).
   - Ensure pip is up-to-date:
     ```bash
     python -m pip install --upgrade pip
     ```

3. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   - Create a `.env` file in the root directory:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. **Run the Flask Application**
   ```bash
   python app.py
   ```
   - Access the application at `http://127.0.0.1:5000/`.

## How to Run

1. **Input Job Description**: Enter the job description in the provided textarea on the web interface.
2. **Specify Resume Folder Path**: Enter the path to the folder containing resumes.
3. **Submit the Form**: The system processes resumes and displays extracted information and rankings.
4. **View Results**: Results are displayed in both raw data and formatted markdown reports.

## Technologies Used

- **Flask**: For building the web application.
- **OpenAI**: For natural language processing.
- **Markdown**: For converting markdown text to HTML.
- **docx2txt & PyPDF2**: For document processing.
- **dotenv**: For managing environment variables.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

By following the setup instructions and utilizing the system's features, users can automate the resume screening process, significantly improving efficiency and accuracy in identifying the most suitable candidates for job roles.
```