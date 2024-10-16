# Automated Code Review Setup

This project integrates automated code review using ESLint, SonarQube, and OpenAI Codex. GitHub Actions are used for continuous integration and automating the review process.

## Tools Used

- **Python**: For integrating OpenAI Codex and automating ESLint and SonarQube processes.
- **Node.js & ESLint**: For checking JavaScript code quality.
- **SonarQube**: For static code analysis using Docker.
- **OpenAI Codex**: For providing code refactoring suggestions.

## Setup Instructions

1. Clone the repository.
2. Set up Python virtual environment.
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
