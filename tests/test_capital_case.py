def capital_case(param_str):
    return param_str.capitalize()


def test_capital_case():
    assert capital_case('justin') == 'Justin'
