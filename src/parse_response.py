import re

def parse_response(response):
    cmd_pattern = r'^\$ .*$'
    file_block_pattern = r'\[\{FILE:(.+?)\}\]\n(.*?)\[/\{FILE\}\]'
    refactoring_pattern = r'\[\{REF:(.+?)\}\]\n(.*?)\[/\{REF\}\]'

    commands = re.findall(cmd_pattern, response, re.MULTILINE)
    file_blocks = re.findall(
        file_block_pattern, response, re.MULTILINE | re.DOTALL)
    refactoring_blocks = re.findall(
        refactoring_pattern, response, re.MULTILINE | re.DOTALL)

    parsed_commands = []

    for cmd in commands:
        parsed_commands.append(('command', cmd[2:]))

    for file_block in file_blocks:
        filename, content = file_block
        parsed_commands.append(('file', filename, content))

    for refactoring_block in refactoring_blocks:
        filename, content = refactoring_block
        parsed_commands.append(('refactoring', filename, content))

    return parsed_commands
