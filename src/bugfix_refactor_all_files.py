import os
from typing import List
from compress_code import compress_code
from chatgpt_query import chatgpt_query
from parse_bugfix_refactoring_response import parse_bugfix_refactoring_response
from recursive_file_search import recursive_file_search
from generate_html_report import generate_html_report


def split_code_into_chunks(code: str, chunk_size: int = 4000) -> List[str]:
    lines = code.split('\n')
    chunks = []

    current_chunk = ""
    for line in lines:
        if len(current_chunk) + len(line) > chunk_size:
            chunks.append(current_chunk.strip())
            current_chunk = ""

        current_chunk += line + "\n"

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks


def bugfix_refactor_all_files():
    file_paths = recursive_file_search()
    print(file_paths)
    all_issues = []
    promt = ""
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            code = f.read()

        compressed_code = compress_code(code)

        # If the compressed code is still too long, split it into chunks
        code_chunks = split_code_into_chunks(compressed_code)

        for chunk in code_chunks:
            command = f"ChatGPT, find bugs and refactoring suggestions in the following {os.path.basename(file_path)} code:\n\n{chunk}"
            promt = f"\nPlease return the line number, issue, and proposed solution for each issue found in the format: 'File: [file_path]\\nLine: [line number]\\nIssue: [issue]\\nSolution: [solution]\\n'. Separate each issue with an empty line."

            response = chatgpt_query(promt)
            issues = parse_bugfix_refactoring_response(response)
            all_issues.extend(issues)

    html_report = generate_html_report(all_issues)
    with open("bugfix_refactoring_report.html", "w") as f:
        f.write(html_report)

    print("Bugfix and refactoring report has been generated: bugfix_refactoring_report.html")
