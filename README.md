# PyCodeQuality

PyCodeQuality is a comprehensive Python package for analyzing and improving code quality. It combines various tools and practices into a single library, making it more convenient for developers to maintain high-quality code. PyCodeQuality provides features such as static analysis, refactoring, best practices enforcement, code complexity analysis, dependency management, code coverage, and documentation analysis.

## Installation

You can install PyCodeQuality using pip:

```bash
pip install pycodequality
Usage
As a library
```python
from pycodequality.static_analysis import analyzer
from pycodequality.refactoring import refactor

# Analyze code for potential issues
issues = analyzer.analyze_code('path/to/your/code.py')

# Refactor the code and receive suggestions
refactored_code = refactor.refactor_code('path/to/your/code.py')
```

As a command-line tool
```bash
python pycodequality_cli.py path/to/your/code.py
```

To refactor the code and save it to a new file, add the -r or --refactor flag:
```bash
python pycodequality_cli.py -r path/to/your/code.py
```

License
This project is licensed under the MIT License. See the LICENSE file for details.