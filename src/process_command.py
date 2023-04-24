import os
import shlex
import subprocess
from bugfix_refactor_all_files import bugfix_refactor_all_files
from chatgpt_query import chatgpt_query
from parse_response import parse_response


def process_command(command_parts):
    global last_request

    if command_parts:
        option = command_parts[0]

        if option == "--bugfix":
            bugfix_refactor_all_files()
            return
        else:
            command = " ".join(command_parts)
            prompt = f"ChatGPT, please provide only the necessary terminal commands or code snippets to {command}, in a clear and concise format for macos. If a file needs to be created, indicate its content using [{{FILE:filename}}]...[/{{FILE}}] format. If a command needs to be executed, indicate it starting with '$ '"
            last_request = command

        response = chatgpt_query(prompt)
        parsed_commands = parse_response(response)

        for cmd_type, *cmd_data in parsed_commands:
            if cmd_type == 'command':
                cmd = cmd_data[0]
                print(f"Executing: {cmd}")

                cmdParts = shlex.split(cmd)
                if cmdParts[0] == 'cd':
                    os.chdir(cmdParts[1])
                else:
                    subprocess.run(cmd, shell=True)
            elif cmd_type == 'file':
                filename, content = cmd_data
                print(f"Writing content to: {filename}")
                with open(filename.strip(), 'w') as f:
                    f.write(content)
    else:
        print("Invalid option. Use --command to send commands.")
