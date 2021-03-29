from leetcode_problem import LeetCodeProblem, GitHubFile, NameUtil


class PythonThreeLeetCodeProblem(LeetCodeProblem):

    def extract_class_docs(self):
        pass

    def setup_source_file(self) -> GitHubFile:
        return GitHubFile(
            # to root dir, snake-case file name
            f"{NameUtil.kebab_case_to_snake_sentence(self.title_slug)}.py",
            f'{self.id}: {self.title_with_space}',
            self.setup_python_three_source_file_content()
        )

    def setup_python_three_source_file_content(self):
        return f'# https://leetcode-cn.com/problems/{self.title_slug}/\n{self.code_snippet}\n'
