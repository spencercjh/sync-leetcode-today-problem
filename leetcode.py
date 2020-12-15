import json

import requests


class NameUtil(object):
    @staticmethod
    def kebab_case_to_upper_camel_case(kebab_str: str) -> str:
        """
        kebab case to upper camel case
        :param kebab_str: example: two-sum
        :return: example: TwoSum
        """
        return ''.join(word.title() for word in kebab_str.split("-")) if kebab_str else ''

    @staticmethod
    def kebab_case_to_camel_sentence(kebab_str: str, separator: str) -> str:
        """
        kebab case to space-separated str
        :param kebab_str: example: two-sum
        :param separator: separator
        :return: example: Two Sum
        """
        return separator.join(word.title() for word in kebab_str.split("-")) if kebab_str else ''


class GitHubFile(object):

    def __init__(self, _path, _message, _content) -> None:
        super().__init__()
        self.path = _path
        self.message = _message
        self.content = _content

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class LeetCodeQuestion(object):

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.file_user = kwargs['user']
        self.id = kwargs['id']
        self.title_slug = kwargs['title_slug']
        self.title_with_space = NameUtil.kebab_case_to_camel_sentence(self.title_slug, ' ')
        self.title_without_space = NameUtil.kebab_case_to_camel_sentence(self.title_slug, '')
        self.code_snippet = ''
        self.function_signature = ''
        self.function_name = ''

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_code_snippet(self, _code_snippet: str):
        self.code_snippet = _code_snippet
        self.function_signature = self.extract_function_signature_from_snippet()
        self.function_name = self.extract_function_name_from_signature()
        return self

    def setup_source_file(self) -> GitHubFile:
        raise NotImplementedError

    def setup_test_file(self) -> GitHubFile:
        raise NotImplementedError

    @staticmethod
    def get_one_language_code_snippets_from_question_data(language: str, _question_data: dict) -> str:
        for snippet in _question_data['codeSnippets']:
            if snippet['lang'] == language:
                return snippet['code']

    def extract_function_name_from_signature(self):
        raise NotImplementedError

    def extract_function_signature_from_snippet(self) -> str:
        raise NotImplementedError


class JavaLeetCodeQuestion(LeetCodeQuestion):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def extract_function_signature_from_snippet(self) -> str:
        return self.code_snippet[self.code_snippet.index('\n'):self.code_snippet.rindex('\n')]

    def extract_function_name_from_signature(self) -> str:
        words = [words for words in self.function_signature.strip().split(' ') if words]
        return words[2][:words[2].rindex('(')]

    def setup_source_file(self) -> GitHubFile:
        # TODO: user
        return GitHubFile(
            f"src/main/java/spencercjh/problems/{self.title_without_space}.java",
            f'{self.id}: {self.title_with_space}',
            self.setup_java_source_file_content()
        )

    def setup_java_source_file_content(self):
        # TODO: user
        return """package spencercjh.problems;
           
import javax.inject.Singleton;
            
/**
 * https://leetcode-cn.com/problems/%s/
 *
 * @author %s
 */
@Singleton
public class %s{
%s

}
""" % (self.title_slug, self.file_user, self.title_without_space, self.function_signature)

    def setup_test_file(self):
        # TODO: user
        return GitHubFile(
            f"src/test/java/spencercjh/problems/{self.title_without_space}Test.java",
            f'{self.id}: {self.title_with_space} (Test)',
            self.setup_java_test_file_content()
        )

    def setup_java_test_file_content(self):
        # TODO: user
        return """package spencercjh.problems;

import io.micronaut.test.extensions.junit5.annotation.MicronautTest;
import org.junit.jupiter.api.Test;

import javax.inject.Inject;

import static org.junit.jupiter.api.Assertions.*;

@MicronautTest
class %sTest {

  @Inject
  private %s solution;
  
  @Test
  void %s() {
    
  }

}
""" % (self.title_without_space, self.title_without_space, self.function_name)


class LeetCodeClient(object):

    def __init__(self, language, user):
        self.csrf_token: str = ''
        self.graphql_url: str = 'https://leetcode-cn.com/graphql'
        self.session = requests.session()
        self.language: str = language
        self.user: str = user

    def question_of_today(self):
        payload = "{\"query\":\"query questionOfToday{\\r\\n" \
                  "    todayRecord{\\r\\n" \
                  "        question{\\r\\n" \
                  "            questionFrontendId\\r\\n" \
                  "            questionTitleSlug\\r\\n" \
                  "        }\\r\\n        " \
                  "date\\r\\n    " \
                  "}\\r\\n" \
                  "}\"," \
                  "\"variables\":{}" \
                  "}"
        headers = {
            'accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.75 Safari/537.36',
            'content-type': 'application/json',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty'
        }
        response = self.session.post(self.graphql_url, headers=headers, data=payload)
        _question = response.json()['data']['todayRecord'][0]['question']
        # example: set-cookie: csrfToken=something; other=something;
        self.csrf_token = response.headers['set-cookie'].split('; ')[0].split('=')[1]
        # FIXME: Not hard code
        if 'java' == self.language.lower():
            return JavaLeetCodeQuestion(
                id=_question['questionFrontendId'],
                title_slug=_question['questionTitleSlug'],
                user=self.user,
            )
        else:
            raise NotImplementedError("Not support this language yet")

    def question_data(self, _title_slug: str) -> dict:
        while not self.csrf_token:
            self.question_of_today()
        body = {
            'operationName': "questionData",
            'variables': {
                'titleSlug': _title_slug
            },
            'query': '''query questionData($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    titleSlug
                    codeSnippets{
                        lang
                        langSlug
                        code
                        __typename
                    }
                }
            }'''
        }

        response = self.session.post(self.graphql_url, headers=self.__get_common_header(_title_slug), json=body)
        return response.json()['data']['question'] if response.status_code == 200 else print(response.content)

    def get_question_detail(self, _title_slug: str) -> dict:
        while not self.csrf_token:
            self.question_of_today()
        body = {
            'operationName': "getQuestionDetail",
            'variables': {'titleSlug': _title_slug},
            'query': '''query getQuestionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    questionFrontendId
                    questionTitle
                    questionTitleSlug
                    content
                    difficulty
                    stats
                    similarQuestions
                    categoryTitle
                    topicTags {
                            name
                            slug
                    }
                }
            }'''
        }

        response = self.session.post(self.graphql_url, headers=self.__get_common_header(_title_slug), json=body)
        return response.json()['data']['question'] if response.status_code == 200 else print(response.content)

    def __get_common_header(self, _title_slug):
        return {
            'x-timezone': 'Asia/Shanghai',
            'x-operation-name': 'questionData',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.75 Safari/537.36',
            'content-type': 'application/json',
            'accept': '*/*',
            'x-csrftoken': f'{self.csrf_token}',
            'x-definition-name': 'question',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': f'https://leetcode.com/problems/{_title_slug}'
        }
