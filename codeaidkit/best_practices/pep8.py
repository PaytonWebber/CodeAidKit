import pycodestyle
import re


def check_pep8(file_path, ignore=None):
    """Check the Python file for PEP8 compliance using pycodestyle."""

    style = pycodestyle.StyleGuide(quite=True, ignore=ignore)
    result = style.check_files([file_path])

    issues = []
    pattern = r'^\d+'
    for issue in result.get_statistics(''):
        frequency = re.search(pattern, issue).group()
        issue = re.sub(pattern, '', issue)
        issue = issue.strip()
        issues.append((issue, frequency))
    return issues
