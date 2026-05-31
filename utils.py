from datetime import date, timedelta
from email_validator import validate_email,EmailNotValidError

def streak_calculator(dates_list):
    if not dates_list:
        return 0
    if str(date.today()) not in dates_list:
        return 0
    current_date=date.today()
    count=0
    while str(current_date) in dates_list:
        count+=1
        current_date=current_date-timedelta(days=1)
    return count


def validate_password(pwd):
    if len(pwd) < 8:
        return "Password must be at least 8 characters"
    if not any(c.isupper() for c in pwd):
        return "Password must have at least 1 uppercase letter"
    if not any(c.isdigit() for c in pwd):
        return "Password must have at least 1 number"
    if not any(c in "!@#$%^&*" for c in pwd):
        return "Password must have at least 1 special character (!@#$%^&*)"
    return None

def validate_email_util(email):
    try:
        email_info = validate_email(email)
        normalized_email = email_info.normalized
        return normalized_email

    except EmailNotValidError as e:
        return None