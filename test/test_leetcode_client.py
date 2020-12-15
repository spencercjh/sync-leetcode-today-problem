from leetcode_client import LeetCodeClient
from leetcode_problem import NameUtil

LANGUAGE = 'Java'
client = LeetCodeClient(LANGUAGE, 'spencercjh')


def test_kebab_case_to_camel_sentence():
    assert 'Two Sum' == NameUtil.kebab_case_to_camel_sentence('two-sum', ' ')
    assert '' == NameUtil.kebab_case_to_camel_sentence('', '')
    # noinspection PyTypeChecker
    assert '' == NameUtil.kebab_case_to_camel_sentence(None, '')
    assert 'TwoSum' == NameUtil.kebab_case_to_camel_sentence('two-sum', '')


def test_today_record():
    today_record = client.question_of_today()
    assert today_record.id
    assert today_record.title_slug
    assert client.csrf_token
    print(today_record)


def test_question_data():
    question_data = client.question_data('two-sum')
    assert question_data
    assert 'titleSlug' in question_data.keys()
    assert 'two-sum' == question_data['titleSlug']
    print(question_data)


def test_get_question_detail():
    question_detail = client.get_question_detail('two-sum')
    assert question_detail
    assert 'two-sum' == question_detail['questionTitleSlug']
