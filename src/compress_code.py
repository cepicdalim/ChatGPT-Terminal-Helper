import re

def compress_code(code: str, language: str = 'python') -> str:
    if language == 'python':
        # Remove comments
        code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)
    elif language in ['javascript', 'typescript', 'java', 'c', 'cpp']:
        # Remove single-line comments
        code = re.sub(r'//.*$', '', code, flags=re.MULTILINE)
        # Remove multi-line comments
        code = re.sub(r'/\*[\s\S]*?\*/', '', code, flags=re.MULTILINE)
    # Remove empty lines
    code = re.sub(r'\n\s*\n', '\n', code)
    return code