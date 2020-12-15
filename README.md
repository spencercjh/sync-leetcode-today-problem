# Sync LeetCode Today Problem

Today Problem (official graphql operation name is Today Record) is a feature only at leetcode-cn.com

## Supported languages right now

- Java

## How to extend more languages

- Add a `.py` file named `<language>_leetcode_problem.py`.For example: `cpp_leetcode_problem.py`.
- Override following methods: `extract_function_signature_from_snippet(self)`, `extract_function_name_from_signature(self)`, `setup_source_file(self)` and `setup_java_source_file_content(self)`.
- Add some test to a new test file named `test_<language>_leetcode_problem.py`, and pay attention to the actual output
 of the generated codes.

