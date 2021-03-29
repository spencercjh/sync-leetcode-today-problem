import json


class GitHubFile(object):
    """
    An abstract of the file to create
    """

    def __init__(self, _path, _message, _content) -> None:
        super().__init__()
        self.path = _path
        self.message = _message
        self.content = _content

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class NameUtil(object):
    """
    name converter
    """

    @staticmethod
    def kebab_case_to_camel_sentence(kebab_str: str, separator: str) -> str:
        """
        kebab case to camel case with a specific separator
        :param kebab_str: example: two-sum
        :param separator: separator like space or None
        :return: example: Two Sum | TwoSum | Two-Sum
        """
        return separator.join(word.title() for word in kebab_str.split("-")) if kebab_str else ''

    @staticmethod
    def kebab_case_to_snake_sentence(kebab_str: str) -> str:
        """
        kebab case to camel case with a specific separator
        :param kebab_str: example: two-sum
        :return: example: two_sum
        """
        return '_'.join(word for word in kebab_str.split("-")) if kebab_str else ''


class LeetCodeProblem(object):
    """
    An abstract of a LeetCode Problem
    """

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
        self.class_docs = ''

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_code_snippet(self, _code_snippet: str):
        self.code_snippet = _code_snippet
        self.modify_the_class_name_in_snippet()
        self.class_docs = self.extract_class_docs()
        return self

    def setup_source_file(self) -> GitHubFile:
        raise NotImplementedError

    @staticmethod
    def get_one_language_code_snippets_from_question_data(language: str, _question_data: dict) -> str:
        for snippet in _question_data['codeSnippets']:
            if snippet['lang'].upper() == language.upper() or snippet['langSlug'].upper() == language.upper():
                return snippet['code']

    def extract_class_docs(self):
        """
        extract class docs from self.code_snippet and remove them from source code
        :return:
        """
        raise NotImplementedError

    def modify_the_class_name_in_snippet(self):
        self.code_snippet = self.code_snippet.replace('Solution', self.title_without_space)
