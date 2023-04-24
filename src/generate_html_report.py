def generate_html_report(issues):
    if not issues:
        return ""

    html_template = '''
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <meta charset="UTF-8">
                        <title>Bugfix and Refactoring Report</title>
                        <style>
                            body { font-family: Arial, sans-serif; }
                            h1 { color: #333; }
                            .issue { border: 1px solid #ccc; border-radius: 4px; margin-bottom: 10px; padding: 10px; }
                            .issue h2 { margin-top: 0; }
                            .issue p { margin: 0; }
                        </style>
                    </head>
                    <body>
                        <h1>Bugfix and Refactoring Report</h1>
                    '''

    for issue in issues:
        html_template += f'''
                                <div class="issue">
                                    <h2>{issue["file_path"]}: Line {issue["line"]}</h2>
                                    <p><strong>Issue:</strong> {issue["issue"]}</p>
                                    <p><strong>Solution:</strong> {issue["solution"]}</p>
                                </div>
                            '''

    html_template += '''
                        </body>
                        </html>
                        '''

    return html_template