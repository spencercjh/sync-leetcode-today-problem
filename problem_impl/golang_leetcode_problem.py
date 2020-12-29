from leetcode_problem import LeetCodeProblem, GitHubFile, NameUtil


class GolangLeetCodeProblem(LeetCodeProblem):
    def extract_function_signature_from_snippet(self) -> str:
        return self.code_snippet[self.code_snippet.index('func'):self.code_snippet.rindex('\n')]

    def extract_function_name_from_signature(self) -> str:
        words = [words for words in self.function_signature.strip().split(' ') if words]
        return words[1][:words[1].rindex('(')]

    def setup_source_file(self) -> GitHubFile:
        return GitHubFile(
            # to root dir, snake-case file name
            f"{NameUtil.kebab_case_to_snake_sentence(self.title_slug)}.go",
            f'{self.id}: {self.title_with_space}',
            self.setup_golang_source_file_content()
        )

    def setup_test_file(self) -> GitHubFile:
        # TODO: TBD
        pass

    def setup_golang_source_file_content(self):
        return f"""// https://leetcode-cn.com/problems/{self.title_slug}
{self.function_signature}
}}
"""
