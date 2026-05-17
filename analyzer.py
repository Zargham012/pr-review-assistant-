import ast
import os
import sys
import json
from pathlib import Path


def find_functions_without_docstrings(file_path):
    """Find all functions in a Python file that are missing docstrings."""
    missing_docs = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read(), filename=file_path)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Check if function has a docstring
                docstring = ast.get_docstring(node)
                if not docstring:
                    missing_docs.append(node.name)
    except Exception as e:
        print(f"Error parsing {file_path}: {e}", file=sys.stderr)
    
    return missing_docs


def find_python_files(folder_path):
    """Recursively find all Python files in the given folder."""
    python_files = []
    folder = Path(folder_path)
    
    if not folder.exists():
        return python_files
    
    for file_path in folder.rglob("*.py"):
        # Skip __init__.py and files in virtual environments
        if file_path.name != "__init__.py" and "venv" not in str(file_path) and "env" not in str(file_path):
            python_files.append(file_path)
    
    return python_files


def find_missing_tests(python_files):
    """Find Python files that don't have corresponding test files."""
    missing_tests = []
    
    for file_path in python_files:
        # Skip test files themselves
        if file_path.name.startswith("test_"):
            continue
        
        # Check for corresponding test file
        test_file_name = f"test_{file_path.name}"
        test_file_path = file_path.parent / test_file_name
        
        # Also check in a tests directory
        tests_dir = file_path.parent / "tests"
        test_file_in_tests_dir = tests_dir / test_file_name
        
        if not test_file_path.exists() and not test_file_in_tests_dir.exists():
            missing_tests.append(str(file_path))
    
    return missing_tests


def analyze_folder(folder_path):
    """Analyze a folder for missing docstrings and tests."""
    python_files = find_python_files(folder_path)
    
    missing_docs = []
    missing_tests = find_missing_tests(python_files)
    
    files_with_missing_docs = 0
    
    for file_path in python_files:
        functions_without_docs = find_functions_without_docstrings(file_path)
        if functions_without_docs:
            files_with_missing_docs += 1
            for func_name in functions_without_docs:
                missing_docs.append(f"{file_path.name}:{func_name}")
    
    # Create summary
    summary = {
        "total_files": len(python_files),
        "files_missing_docs": files_with_missing_docs,
        "files_missing_tests": len(missing_tests),
        "total_functions_missing_docs": len(missing_docs)
    }
    
    # Create report
    report = {
        "missing_docs": missing_docs,
        "missing_tests": missing_tests,
        "summary": summary
    }
    
    return report


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "Please provide a folder path as an argument"
        }))
        sys.exit(1)
    
    folder_path = sys.argv[1]
    
    if not os.path.exists(folder_path):
        print(json.dumps({
            "error": f"Folder path does not exist: {folder_path}"
        }))
        sys.exit(1)
    
    report = analyze_folder(folder_path)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

# Made with Bob
