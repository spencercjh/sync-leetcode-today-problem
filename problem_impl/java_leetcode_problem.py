from leetcode_problem import LeetCodeProblem, GitHubFile


class JavaLeetCodeProblem(LeetCodeProblem):

    def extract_function_signature_from_snippet(self) -> str:
        return self.code_snippet[self.code_snippet.index('\n'):self.code_snippet.rindex('\n')]

    def extract_function_name_from_signature(self) -> str:
        words = [words for words in self.function_signature.strip().split(' ') if words]
        return words[2][:words[2].rindex('(')]

    def setup_source_file(self) -> GitHubFile:
        return GitHubFile(
            f"src/main/java/{self.file_user}/problems/{self.title_without_space}.java",
            f'{self.id}: {self.title_with_space}',
            self.setup_java_source_file_content()
        )

    def setup_java_source_file_content(self):
        return f"""package {self.file_user}.problems;

/**
 * https://leetcode-cn.com/problems/{self.title_slug}/
 *
 * @author {self.file_user}
 */
public class {self.title_without_space} {{
{self.function_signature}

}}
"""

    def setup_test_file(self):
        return GitHubFile(
            f"src/test/java/{self.file_user}/problems/{self.title_without_space}Test.java",
            f'{self.id}: {self.title_with_space} (Test)',
            self.setup_java_test_file_content()
        )

    def setup_java_test_file_content(self):
        return f"""package {self.file_user}.problems;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class {self.title_without_space}Test {{

  private {self.title_without_space} solution = new {self.title_without_space}();
  
  @Test
  void {self.function_name}() {{
    
  }}

}}
"""
