from leetcode_problem import LeetCodeProblem, GitHubFile, NameUtil


class PythonThreeLeetCodeProblem(LeetCodeProblem):

    def extract_function_signature_from_snippet(self) -> str:
        class_end = self.code_snippet.index('class Solution:') + len('class Solution:')
        return self.code_snippet[class_end:]

    def extract_function_name_from_signature(self):
        words = [words for words in self.function_signature.strip().split(' ') if words]
        return words[1][:words[1].rindex('(')]

    def setup_source_file(self) -> GitHubFile:
        return GitHubFile(
            # to root dir, snake-case file name
            f"{NameUtil.kebab_case_to_snake_sentence(self.title_slug)}.py",
            f'{self.id}: {self.title_with_space}',
            self.setup_python_three_source_file_content()
        )

    def setup_python_three_source_file_content(self):
        return f'''
class {self.title_without_space}:
    """
    {f'https://leetcode-cn.com/problems/{self.title_slug}/'}
    """
    
    {self.function_signature}
'''

    def setup_test_file(self) -> GitHubFile:
        return GitHubFile(
            # to root dir, snake-case file name
            f"test/test_{NameUtil.kebab_case_to_snake_sentence(self.title_slug)}.py",
            f'{self.id}: {self.title_with_space} (Test)',
            self.setup_python_three_test_file_content()
        )

    def setup_python_three_test_file_content(self):
        return f'''solution = {self.title_without_space}()
assert X == solution.{self.function_name}( )'''
