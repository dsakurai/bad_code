#!/usr/bin/python3

def age_in_days(birthday, today):
    """
        誕生日から日齢を計算する
        - 例: age_in_days("1900-01-01", "2021-09-03")
        - birthday: "YYYY-MM-DD" か "DD/MM/YYYY" の形式の誕生日の文字列
        - today:    "YYYY-MM-DD" か "DD/MM/YYYY" の形式の今日の日付の文字列
    """
    
    # 入力がおかしい？
    if (birthday == "") or (len(birthday) != len("1900-01-01")) or (birthday[4] != "-") or (birthday[4] != "/"):
        # Yes => 処理について３つの候補がある。
        
        # 1. 例外を吐いて吐いて終了
        # raise Exception("Bad input")
        
        # 2. None を返す
        # return None
        
        # 3. プログラムごと終了
        print("Bad input.")
        exit(1)
        
        # 今の実装は仮に 3. としておく。

        
    # 誕生日の年月日
    
    # 年月日が "-" で区切られている？
    if birthday[4] == "-":
        # Yes => year, month, day を取得
        year  = birthday.split("-")[0]
        month = birthday.split("-")[1]
        day   = birthday.split("-")[2]
    
    # 年月日が "/" で区切られている？
    elif birthday[4] == "/":
        # day/month/year の形式
        year  = birthday.split("/")[0]
        month = birthday.split("/")[1]
        day   = birthday.split("/")[2]
    
    # 今日の年月日
    t_year  = today.split("-")[0]
    t_month = today.split("-")[1]
    t_day   = today.split("-")[2]
    
    # 年の差
    diff_years = 365 * float(t_year) - float(year)
    
    # 月の差
    diff_months = 31 * float(t_month) - float(month)
    
    # 日の差
    diff_days = float(t_day) - float(day)
    
    return diff_years + diff_months  + diff_days

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
