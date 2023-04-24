import sys
from parse_response import parse_response
from compress_code import compress_code
from chatgpt_query import chatgpt_query
from parse_bugfix_refactoring_response import parse_bugfix_refactoring_response
from bugfix_refactor_all_files import bugfix_refactor_all_files
from process_command import process_command
from recursive_file_search import recursive_file_search
from generate_html_report import generate_html_report

def main():
    if len(sys.argv) > 1:
        option = sys.argv[1]
    process_command(sys.argv[1:])

if __name__ == "__main__":
    main()
