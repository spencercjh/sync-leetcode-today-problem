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
