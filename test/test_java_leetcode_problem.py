from leetcode_client import LeetCodeClient
from leetcode_problem import LeetCodeProblem

LANGUAGE = 'Java'
client = LeetCodeClient(LANGUAGE, 'spencercjh')


def test_multiple_methods_scenario():
    question_of_today = client.question_of_today()
    assert client.csrf_token
    question_data = client.question_data('kth-largest-element-in-a-stream')
    question_of_today.set_code_snippet(
        LeetCodeProblem.get_one_language_code_snippets_from_question_data(LANGUAGE, question_data))

    _common_test(question_of_today)


def test_tree_scenario():
    question_of_today = client.question_of_today()
    assert client.csrf_token
    question_data = client.question_data('balanced-binary-tree')
    question_of_today.set_code_snippet(
        LeetCodeProblem.get_one_language_code_snippets_from_question_data(LANGUAGE, question_data))

    _common_test(question_of_today)


def test_whole_scenario():
    question_of_today = client.question_of_today()
    assert client.csrf_token
    question_data = client.question_data(question_of_today.title_slug)
    question_of_today.set_code_snippet(
        LeetCodeProblem.get_one_language_code_snippets_from_question_data(LANGUAGE, question_data))

    _common_test(question_of_today)


def _common_test(question_of_today):
    assert question_of_today.id
    assert question_of_today.title_slug
    assert question_of_today.title_with_space
    assert question_of_today.title_without_space
    assert question_of_today.file_user
    assert question_of_today.code_snippet
    print(question_of_today.to_json())
    source_file = question_of_today.setup_source_file()
    assert source_file.path
    assert source_file.message
    assert source_file.content
    assert 'None' not in source_file.content
    assert 'Solution' not in source_file.content
    assert 'None' not in source_file.message
    assert 'None' not in source_file.path
    print(source_file.to_json())
    print(source_file.content)
