
# Senitizer
# FilenameSanitizer

A Python utility to handle platform-specific filename sanitization and deprecation warnings.

## Features

- Provides platform-aware sanitization logic for filenames.
- Issues warnings for deprecated callable usage.
- Ensures compatibility across Windows and non-Windows platforms.
- Demonstrates clean and maintainable code practices.

## Usage

```python
from src.sanitizer import sanitize_filename

# Example usage
sanitize = sanitize_filename(key="example", value="unsafe/filename")
print(sanitize)  # Prints sanitized filename
