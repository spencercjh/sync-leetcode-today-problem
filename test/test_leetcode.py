from leetcode_client import LeetCodeClient
from leetcode_problem import LeetCodeProblem, NameUtil

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


def test_whole_scenario():
    question_of_today = client.question_of_today()
    assert client.csrf_token
    question_data = client.question_data(question_of_today.title_slug)
    question_of_today.set_code_snippet(
        LeetCodeProblem.get_one_language_code_snippets_from_question_data(LANGUAGE, question_data))

    assert question_of_today.id
    assert question_of_today.title_slug
    assert question_of_today.title_with_space
    assert question_of_today.title_without_space
    assert question_of_today.file_user
    assert question_of_today.code_snippet
    assert question_of_today.function_name
    assert question_of_today.function_signature

    print(question_of_today.to_json())

    source_file = question_of_today.setup_source_file()
    assert source_file.path
    assert source_file.message
    assert source_file.content

    assert 'None' not in source_file.content
    assert 'None' not in source_file.message
    assert 'None' not in source_file.path

    test_file = question_of_today.setup_test_file()
    assert test_file.path
    assert test_file.message
    assert test_file.content

    assert 'None' not in test_file.content
    assert 'None' not in test_file.message
    assert 'None' not in test_file.path

    print(source_file.to_json())
    print(source_file.content)

    print(test_file.to_json())
    print(test_file.content)
