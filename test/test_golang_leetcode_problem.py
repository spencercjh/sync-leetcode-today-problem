from leetcode_client import LeetCodeClient
from leetcode_problem import LeetCodeProblem

LANGUAGE = 'Golang'
client = LeetCodeClient(LANGUAGE, 'spencercjh')


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

    print(source_file.to_json())
    print(source_file.content)

    # test_file = question_of_today.setup_test_file()
    # assert test_file.path
    # assert test_file.message
    # assert test_file.content
    #
    # assert 'None' not in test_file.content
    # assert 'None' not in test_file.message
    # assert 'None' not in test_file.path
    #

    #
    # print(test_file.to_json())
    # print(test_file.content)
