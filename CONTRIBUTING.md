# Contributing to Image Editor Pro

Thank you for your interest in contributing to Image Editor Pro! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in the Issues section
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable
   - Your environment (OS, Python version, etc.)

### Suggesting Enhancements

1. Check if the enhancement has already been suggested
2. Create a new issue with:
   - Clear title and description
   - Use case and benefits
   - Possible implementation approach (optional)

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Write or update tests as needed
5. Ensure all tests pass
6. Update documentation if needed
7. Commit your changes (`git commit -am 'Add some feature'`)
8. Push to the branch (`git push origin feature/your-feature-name`)
9. Create a Pull Request

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/image-editor-pro.git
   cd image-editor-pro
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run tests:
   ```bash
   python test_basic.py
   ```

## Code Style

- Follow PEP 8 style guidelines
- Use descriptive variable and function names
- Add docstrings to all classes and functions
- Keep functions focused and single-purpose
- Comment complex logic

## Testing

- Write tests for new features
- Ensure existing tests still pass
- Test on multiple platforms if possible

## Documentation

- Update README.md for new features
- Add docstrings to new code
- Update inline comments as needed

## Questions?

Feel free to open an issue for any questions about contributing!
