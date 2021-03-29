from leetcode_problem import LeetCodeProblem, GitHubFile, NameUtil


class GolangLeetCodeProblem(LeetCodeProblem):

    def extract_class_docs(self):
        if self.code_snippet.startswith('/**'):
            docs = self.code_snippet[
                   self.code_snippet.index('/**'):self.code_snippet.index('*/') + len('*/')] \
                .replace('/**', f'/**\n * https://leetcode-cn.com/problems/{self.title_slug}/\n *')
            self.code_snippet = self.code_snippet[self.code_snippet.index('*/') + len('*/'):]
            return docs
        else:
            return f'// https://leetcode-cn.com/problems/{self.title_slug}/'

    def modify_the_class_name_in_snippet(self):
        pass

    def setup_source_file(self) -> GitHubFile:
        return GitHubFile(
            # to root dir, snake-case file name
            f"{NameUtil.kebab_case_to_snake_sentence(self.title_slug)}.go",
            f'{self.id}: {self.title_with_space}',
            self.setup_golang_source_file_content()
        )

    def setup_golang_source_file_content(self):
        return f'package leetcode\n\n{self.class_docs}\n{self.code_snippet}\n'
