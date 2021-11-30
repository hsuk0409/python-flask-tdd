from datetime import datetime, date, timedelta


def convert_datetime_to_date_str(dt: datetime) -> str:
    datetime_str = str(dt.date())

    print("Start converting!!")
    print(datetime_str)

    return datetime_str


def test_convert_datetime():
    result = str(datetime.now().date())
    assert convert_datetime_to_date_str(datetime.now()) == result


def test_date_today():
    today = date.today()
    tomorrow = today + timedelta(1)
    print()
    print(f"today:: {today}")
    print(f"tomorrow:: {tomorrow}")

    assert tomorrow > today


def test_str_date_convert():
    str_date = "2021-11-30"
    converted_date = datetime.strptime(str_date, "%Y-%m-%d").date()

    print(f"converted_date:: {converted_date}")

