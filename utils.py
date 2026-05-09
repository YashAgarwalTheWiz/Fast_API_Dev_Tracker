from datetime import date, timedelta
import calendar

def streak_calculator(dates):
    if not dates:
        return 0
    dates_list=[row[0] for row in dates]
    if str(date.today()) not in dates_list:
        return 0
    current_date=date.today()
    count=0
    while str(current_date) in dates_list:
        count+=1
        current_date=current_date-timedelta(days=1)
    return count

