import os

def recursive_file_search(path="."):
    allowed_extensions = ['.dart', '.cs', '.py', '.php', '.js', '.ts',
                          '.java', '.cpp', '.c', '.rb', '.go', '.swift', '.sql', '.yml', '.yaml']
    excluded_directories = [
        'node_modules', '__pycache__', '.git', '.svn', '.hg', 'venv', 'dist', 'build', '.vscode', '.idea', 'target', 'out',
        'bower_components', 'vendor', 'packages', '.nuget', '.gradle', '.caches', 'tmp', '.cache', '.pytest_cache', '.mypy_cache',
        'deps', '_build', 'ebin', '_rel', 'Debug', 'Release', '.metadata', '.recommenders', 'android', 'ios'
    ]
    file_paths = []

    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in excluded_directories]

        for file in files:
            file_path = os.path.join(root, file)
            _, file_extension = os.path.splitext(file_path)

            if file_extension in allowed_extensions:
                file_paths.append(file_path)

    return file_paths