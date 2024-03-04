import upper_and_lower_case


def test_count_of_lower_and_upper_case():
    assert upper_and_lower_case.count_upper_and_lower_case_two("Hello world") == {'UPPER CASE': 1,
                                                                                  'LOWER CASE': 9}
