1. Which issues were the easiest to fix, and which were the hardest? Why? 
    The easiest fixes were naming and spacing (PEP 8) changes. The hardest were replacing eval() and handling the bare except, since they needed safe, logic-level updates.
2. Did the static analysis tools report any false positives? If so, describe one example.
    Yes, there was one minor false positive related to the global variable usage which was not a real issue for this small script
3. How would you integrate static analysis tools into your actual software development 
    workflow? Consider continuous integration (CI) or local development practices. 
    I would integrate static analysis tools in actual software development workflow by running tools like pylint, flake8, and bandit as pre-commit checks locally and in CI pipelines to catch issues before merging code.
4. What tangible improvements did you observe in the code quality, readability, or potential 
    robustness after applying the fixes?
    the improvements observed were :- Code became cleaner, more secure, and easier to read after adding docstrings, fixing style issues, and removing unsafe code
