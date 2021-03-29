from leetcode_client import LeetCodeClient
from leetcode_problem import LeetCodeProblem
from test.test_leetcode_problem import _common_test

LANGUAGE = 'Golang'
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
