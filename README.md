# Sync LeetCode Today Problem

![Lint and Test](https://github.com/spencercjh/sync-leetcode-today-problem/workflows/Lint%20and%20Test/badge.svg)

Today Problem (official graphql operation name is Today Record) is a feature only at leetcode-cn.com.

Are you missing the smart IDE during your coding on the web? Do you think the solution is more important than the form of coding such as whiteboard-coding?

**Try this Github Action!**

This action will create a source file and a test file(optional) of the problem. Currently the file path is not configurable. (A configurable path for file generation would greatly increase the flexibility of this Action. I will solve it in the near future.) For example, in Cpp and Python, files are added to the root directory, the Pytest files are created in test directory. It takes you a little time to get more info from the example.

This action can be used not only in empty repo, but also in your existing leetcode solutions repository. 

## Supported languages right now

- Java:[example](https://github.com/spencercjh/sync-leetcode-today-problem-java-example)
- Cpp:[example](https://github.com/spencercjh/sync-leetcode-today-problem-cpp-example) (not support test file now)
- Python3:[example](https://github.com/spencercjh/sync-leetcode-today-problem-python3-example)

## Workflow example

```yaml
name: Sync LeetCode Today Problem

on:
  workflow_dispatch:
  schedule:
    # Runs at 00:01 UTC+8
    - cron: "1 16 * * *"

jobs:
  sync_leetcode_today_record_job:
    name: sync leetcode today problem job
    runs-on: ubuntu-latest
    steps:
      - name: Sync LeetCode Today Problem
        uses: spencercjh/sync-leetcode-today-problem@<latest version>
        with:
          language: Java
          need_test: True

```

## Parameters

### Optional

- github_token
- repository
- branch
- user

### Required

- language: which language of code snippet you want to generate.
- need_test: whether need test file

## Welcome issues and PR to extend more languages

**If you think it is valuable and meaningful to solve LeetCode Today Problem(record or question, whatever you like to name it in English) with VCS, let Github to record your daily use of LeetCode, welcome to contribute this little project.**

The language format is **upper-camel-case**. Here are the examples: `Cpp`,`JavaScript`,`Php`,`Kotlin`. The language name in the python file name has to obey python style: **snake-case** , for example: `cpp_leetcode_problem.py`.

- Add a `.py` file named `<language>_leetcode_problem.py`.For example: `cpp_leetcode_problem.py`.
- Override following methods: `extract_function_signature_from_snippet(self)`, `extract_function_name_from_signature(self)`, `setup_source_file(self)` and `setup_test_file(self)`.
- Add a `language-Class` mapping to the `supported_language:dict` at the top of the  `leetcode_client.py` like `'JAVA': JavaLeetCodeProblem`.
- Add some test to a new test file named `test_<language>_leetcode_problem.py`, and pay attention to the actual output
 of the generated codes.
- Update the associated content in `README.md`.
