from repository.user_repository import get_user_id
from repository.problem_repository import show_single_user_value,insert_entries,get_difficulty_count,piechartbytopic,dates_user_active,filter_by_difficulty

def get_user_problems(email,page,limit):
    user_id=get_user_id(email)
    user_problems=show_single_user_value(user_id,page,limit)
    return user_problems

def log_problem(data,email):
    user_id=get_user_id(email)
    insert_entries(data,user_id)

def get_difficulty_stats(email):
    user_id=get_user_id(email)
    return get_difficulty_count(user_id)

def get_topic_stats(email):
    user_id=get_user_id(email)
    return piechartbytopic(user_id)

def get_active_dates(email):
    user_id=get_user_id(email)
    return dates_user_active(user_id)

def get_filtered_by_difficulty(difficulty,email):
    user_id=get_user_id(email)
    return filter_by_difficulty(difficulty=difficulty,user_id=user_id)