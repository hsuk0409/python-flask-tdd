from datetime import datetime


def convert_datetime_to_date_str(dt: datetime) -> str:
    datetime_str = str(dt.date())

    print("Start converting!!")
    print(datetime_str)

    return datetime_str


def test_convert_datetime():
    result = '2021-10-21'
    assert convert_datetime_to_date_str(datetime.now()) == result
