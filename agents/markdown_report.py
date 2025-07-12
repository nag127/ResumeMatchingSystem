def generate_markdown(summaries):
    parsed = []
    for summary in summaries:
        lines = summary.split('\n')
        score_str = lines[1].replace("- Relevance Score:", "").strip()
        score = int(score_str.split('/')[0]) if '/' in score_str else int(score_str)
        data = {
            "name": lines[0].replace("- Name:", "").strip(),
            "score": score,
            "summary": lines[2].replace("- Summary:", "").strip()
        }
        parsed.append(data)

    parsed.sort(key=lambda x: x['score'], reverse=True)

    markdown = "## 📝 Resume Rankings\n\n"
    for idx, p in enumerate(parsed, start=1):
        markdown += f"### {idx}. {p['name']} – Score: {p['score']}/10\n"
        markdown += f"- **Summary**: {p['summary']}\n\n---\n"
    return markdown
