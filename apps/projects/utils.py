import secrets

def flight_task_id():
    return secrets.token_urlsafe(8)