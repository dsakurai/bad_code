import datetime

# Unit test の例
def square(x):
    """
    Calculate the square of x.

    >>> square(2)
    4
    >>> square(-2)
    4
    """

    return x * x

def age_in_days(birthday, today):
    """
        誕生日から日齢を計算する

        - 例: age_in_days("1900-01-01", "2021-09-03")
        - birthday: "YYYY-MM-DD" の 形式の誕生日の文字列
        - today: "YYYY-MM-DD" の 形式の今日の文字列
    """

    if birthday == "":
        # raise Exception("Bad input")
        print("Bad input.")
        exit(1)
        # return None

    # 誕生日の年月日
    year, month, day = birthday.split("-")

    # 今日の年月日
    t_year, t_month, t_day = today.split("-")

    # 年の差
    diff_years = 365 * float(t_year) - float(year)

    # 月の差
    diff_months = 31 * float(t_month) - float(month)

    # 日の差
    diff_days = float(t_day) - float(day)

    return diff_years + diff_months  + diff_days

x = 3

age = age_in_days("", "2000-03-01")

print(age)

# if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
