import requests

from java_leetcode_problem import JavaLeetCodeProblem

# Add language-Class mapping here
supported_language: dict = {'JAVA': JavaLeetCodeProblem}


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

        if self.language.upper() in supported_language.keys():
            return supported_language[self.language.upper()](id=_question['questionFrontendId'],
                                                             title_slug=_question['questionTitleSlug'],
                                                             user=self.user, )
        else:
            raise NotImplementedError(f'Not support this language:{self.language} yet')

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
