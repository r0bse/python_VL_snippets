from functools import wraps

from flask import render_template, session


def is_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if("username" in session):
            return func(*args, **kwargs)
        return render_template("forbidden.html")
    return wrapper