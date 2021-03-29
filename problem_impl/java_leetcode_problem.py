from leetcode_problem import LeetCodeProblem, GitHubFile


class JavaLeetCodeProblem(LeetCodeProblem):

    def setup_source_file(self) -> GitHubFile:
        return GitHubFile(
            f"src/main/java/{self.file_user}/problems/{self.title_without_space}.java",
            f'{self.id}: {self.title_with_space}',
            self.setup_java_source_file_content()
        )

    def extract_class_docs(self):
        if self.code_snippet.startswith('/**'):
            docs = self.code_snippet[
                   self.code_snippet.index('/**'):self.code_snippet.index('*/') + len('*/')] \
                .replace('/**', f'/**\n * https://leetcode-cn.com/problems/{self.title_slug}/\n *') \
                .replace("*/\n\n", f'* \n * @author {self.file_user}\n */')
            self.code_snippet = self.code_snippet[self.code_snippet.index('*/') + len('*/'):]
            return docs
        else:
            return f'/**\n * https://leetcode-cn.com/problems/{self.title_slug}/\n * \n * @author {self.file_user}\n */'

    def setup_java_source_file_content(self):

        return f'package {self.file_user}.problems;\n\n{self.class_docs}\n{self.code_snippet}\n'
