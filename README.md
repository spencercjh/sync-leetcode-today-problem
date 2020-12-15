# Sync LeetCode Today Problem

Today Problem (official graphql operation name is Today Record) is a feature only at leetcode-cn.com

## Parameters

### Optional

- github_token
- repository
- branch
- user

### Required

- language: which language of codes you want to generate.

## Supported languages right now

- Java

## Workflow example

Or you can go to the [example repo](https://github.com/spencercjh/sync-leetcode-today-problem-example) for more details.

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
        uses: spencercjh/sync-leetcode-today-problem@0.0.1
        with:
          language: Java
```

## How to extend more languages

The language format is **upper-camel-case**. Here are the examples: `Cpp`,`JavaScript`,`Php`,`Kotlin`. The language name in the python file name has to obey python style: **snake-case** , for example: `cpp_leetcode_problem.py`.

- Add a `.py` file named `<language>_leetcode_problem.py`.For example: `cpp_leetcode_problem.py`.
- Override following methods: `extract_function_signature_from_snippet(self)`, `extract_function_name_from_signature(self)`, `setup_source_file(self)` and `setup_test_file(self)`.
- Add some test to a new test file named `test_<language>_leetcode_problem.py`, and pay attention to the actual output
 of the generated codes.

