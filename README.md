# 🤖 Smart PR Review Assistant

A powerful Python code analysis tool that helps developers identify missing docstrings and test coverage in their projects. Built with IBM Bob to streamline code quality checks before pull requests.

## 📋 Problem It Solves

Code reviews often catch the same recurring issues:
- **Missing Documentation**: Functions without docstrings make code harder to understand and maintain
- **Lack of Test Coverage**: Files without corresponding test files increase the risk of bugs
- **Manual Review Overhead**: Reviewers spend time identifying basic quality issues instead of focusing on logic and architecture

Smart PR Review Assistant automates these checks, providing instant feedback on:
- Functions missing docstrings
- Python files without test coverage
- Comprehensive statistics about your codebase quality

## 🛠️ How IBM Bob Was Used to Build This Project

This entire project was built using **IBM Bob**, an AI-powered development assistant. Bob helped with:

1. **Architecture Design**: Structured the project with a Flask backend API and a clean HTML/CSS/JavaScript frontend
2. **Code Implementation**: 
   - Created the Python AST-based analyzer for detecting missing docstrings
   - Built the Flask REST API with proper error handling
   - Designed a modern, responsive UI with gradient styling
3. **Best Practices**: Implemented proper error handling, CORS support, and timeout management
4. **Documentation**: Generated comprehensive docstrings for all functions

Bob accelerated development by providing instant code generation, debugging assistance, and architectural guidance throughout the entire build process.

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 How to Run

### 1. Start the Backend Server

Run the Flask server:
```bash
python server.py
```

You should see:
```
Starting Smart PR Review Assistant Server...
Server running on http://localhost:5000
```

The server will run on `http://localhost:5000` and provides two endpoints:
- `POST /analyze` - Analyzes a folder for code quality issues
- `GET /health` - Health check endpoint

### 2. Open the Frontend

Open `index.html` in your web browser:
- **Windows**: Double-click `index.html` or right-click → Open with → Your browser
- **Mac/Linux**: Open from terminal: `open index.html` (Mac) or `xdg-open index.html` (Linux)
- **Alternative**: Drag and drop `index.html` into your browser window

### 3. Analyze Your Code

1. Enter the full path to your Python project folder (e.g., `C:\projects\myapp` or `/home/user/projects/myapp`)
2. Click **"🔍 Analyze with Bob"**
3. View the results:
   - **Missing Docstrings**: Functions that need documentation
   - **Missing Tests**: Files without corresponding test files
   - **Summary**: Overall statistics about your codebase

## 📊 Features

- **AST-Based Analysis**: Uses Python's Abstract Syntax Tree for accurate function detection
- **Recursive Scanning**: Automatically finds all Python files in subdirectories
- **Smart Filtering**: Excludes virtual environments and `__init__.py` files
- **Test Detection**: Checks for both adjacent test files and tests in dedicated `tests/` directories
- **Modern UI**: Clean, responsive interface with real-time feedback
- **Error Handling**: Comprehensive error messages for troubleshooting

## 🏗️ Project Structure

```
pr-review-assistant/
├── analyzer.py          # Core analysis logic using Python AST
├── server.py           # Flask REST API server
├── index.html          # Frontend web interface
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔧 API Reference

### POST /analyze

Analyzes a folder for missing docstrings and tests.

**Request Body**:
```json
{
  "folder_path": "/path/to/your/project"
}
```

**Response**:
```json
{
  "missing_docs": ["file.py:function_name", ...],
  "missing_tests": ["/path/to/file.py", ...],
  "summary": {
    "total_files": 10,
    "files_missing_docs": 3,
    "files_missing_tests": 5,
    "total_functions_missing_docs": 8
  }
}
```

### GET /health

Health check endpoint.

**Response**:
```json
{
  "status": "healthy",
  "service": "Smart PR Review Assistant"
}
```

## 🎯 Use Cases

- **Pre-PR Checks**: Run before creating pull requests to ensure code quality
- **CI/CD Integration**: Integrate into your pipeline for automated quality gates
- **Code Reviews**: Help reviewers focus on logic instead of documentation issues
- **Onboarding**: Help new team members understand documentation standards
- **Technical Debt**: Identify areas needing documentation improvements

## 🤝 Contributing

This project was built with IBM Bob. To contribute:
1. Fork the repository
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## 📝 License

This project is open source and available for educational and commercial use.

## 🙏 Acknowledgments

Built entirely with **IBM Bob** - demonstrating the power of AI-assisted development for rapid prototyping and production-ready applications.

---

**Made with ❤️ and IBM Bob**