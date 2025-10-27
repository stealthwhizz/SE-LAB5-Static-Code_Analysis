# Lab Reflection

1. **Easiest and Hardest Issues to Fix**
   - The easiest issues to fix were style-related problems, such as renaming functions to snake_case, adding missing docstrings, and correcting line lengths or blank lines. These changes are straightforward and do not affect program logic.
   - The hardest issues were those involving logic or security, such as input validation, replacing bare `except:` with specific exceptions, and ensuring proper use of context managers for file operations. These required a deeper understanding of the code's intent and potential edge cases.

2. **False Positives from Static Analysis Tools**
   - Yes, there were some false positives. For example, Pylint flagged the use of the `global` statement as a design issue. While generally discouraged, it was necessary in this context to allow functions to modify the shared `stock_data` variable, and refactoring to avoid it would have added unnecessary complexity for a small script.

3. **Integrating Static Analysis Tools into Workflow**
   - I would integrate static analysis tools into both local development and CI pipelines. Locally, I would run tools like Flake8, Pylint, and Bandit before committing code to catch issues early. In CI, I would configure automated checks to run these tools on every pull request, enforcing code quality and security standards before merging.

4. **Tangible Improvements Observed**
   - After applying the fixes, the code became more robust and secure, with better input validation and error handling. Readability improved due to consistent naming, added docstrings, and adherence to PEP8. The code is now easier to maintain, less prone to bugs, and safer against common security pitfalls.
