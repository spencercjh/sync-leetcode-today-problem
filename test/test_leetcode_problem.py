from leetcode_problem import NameUtil


def test_kebab_case_to_camel_sentence():
    assert 'Two Sum' == NameUtil.kebab_case_to_camel_sentence('two-sum', ' ')
    assert '' == NameUtil.kebab_case_to_camel_sentence('', '')
    # noinspection PyTypeChecker
    assert '' == NameUtil.kebab_case_to_camel_sentence(None, '')
    assert 'TwoSum' == NameUtil.kebab_case_to_camel_sentence('two-sum', '')


def test_kebab_case_to_snake_sentence():
    assert 'two_sum' == NameUtil.kebab_case_to_snake_sentence('two-sum')
    assert '' == NameUtil.kebab_case_to_snake_sentence('')
    # noinspection PyTypeChecker
    assert '' == NameUtil.kebab_case_to_snake_sentence(None)


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
    assert 'Solution' not in source_file.content
    assert 'None' not in source_file.message
    assert 'None' not in source_file.path
    print(source_file.to_json())
    print(source_file.content)
