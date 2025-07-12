def format_summary_markdown(name, score, summary):
    return f"### {name} – Score: {score}/10\n- **Summary**: {summary}\n\n---\n"

def format_markdown_report(parsed_data):
    parsed_data.sort(key=lambda x: x['score'], reverse=True)
    markdown = "## \ud83d\udcdc Resume Rankings\n\n"
    for person in parsed_data:
        markdown += format_summary_markdown(person['name'], person['score'], person['summary'])
    return markdown