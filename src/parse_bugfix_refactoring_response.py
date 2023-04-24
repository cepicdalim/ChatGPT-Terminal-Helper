import re;

def parse_bugfix_refactoring_response(response):
    pattern = r'File: (.+?)\nLine: (\d+)\nIssue: (.+?)\nSolution: (.+?)$'
    matches = re.findall(pattern, response, re.MULTILINE | re.DOTALL)
    issues = []

    for match in matches:
        file_path, line_number, issue, solution = match

        issues.append({
            "file_path": file_path.strip(),
            "line": int(line_number),
            "issue": issue.strip(),
            "solution": solution.strip()
        })

    return issues

