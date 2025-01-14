# Sanitizer Project

## Overview
The Sanitizer project provides a robust solution for cleaning and validating user input. It includes a `Sanitizer` class that offers methods to sanitize and validate input data, ensuring that applications can handle user input securely and effectively.

## Features
- **Sanitize Input**: Cleans user input to remove unwanted characters and formats.
- **Validate Input**: Checks the validity of input data against predefined criteria.

## Installation
To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage
To use the `Sanitizer` class, you can import it from the `src` module:

```python
from src.sanitizer import Sanitizer

sanitizer = Sanitizer()
clean_input = sanitizer.sanitize_input(user_input)
is_valid = sanitizer.validate_input(clean_input)
```

## Running Tests
To run the unit tests for the sanitizer functionality, navigate to the `tests` directory and execute:

```
python -m unittest test_sanitizer.py
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.