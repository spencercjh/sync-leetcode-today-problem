from leetcode_problem import LeetCodeProblem, GitHubFile, NameUtil


class CppLeetCodeProblem(LeetCodeProblem):

    def extract_function_signature_from_snippet(self) -> str:
        signature_identifier = 'public:\n'
        begin = self.code_snippet.index(signature_identifier) + len(signature_identifier)
        end = self.code_snippet.rindex('\n')
        return self.code_snippet[begin:end]

    def extract_function_name_from_signature(self):
        words = [words for words in self.function_signature.strip().split(' ') if words]
        return words[1][:words[1].rindex('(')]

    def setup_source_file(self) -> GitHubFile:
        return GitHubFile(
            # to root dir, snake-case file name
            f"{NameUtil.kebab_case_to_snake_sentence(self.title_slug)}.cpp",
            f'{self.id}: {self.title_with_space}',
            self.setup_cpp_source_file_content()
        )

    def setup_cpp_source_file_content(self):
        return f"""/**
 * https://leetcode-cn.com/problems/{self.title_slug}/
 *
 * @author {self.file_user}
 */
class {self.title_without_space} {{
public:
{self.function_signature}

}}
"""

    def setup_test_file(self) -> GitHubFile:
        # TODO: TBD
        pass
