def ignore_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return None
    return wrapper