
_sequence = 1

def _seq():
    global _sequence
    _sequence += 1
    return f"{_sequence:03d}"

import data.articles as articles

def get_user():
    seq = _seq()
    return {
        "email": make_email(seq),
        "password": "password",
        "username": make_username(seq),
    }

def make_email(seq):
    return f"john.q.customer-{seq}@abysmal.com"

def make_username(seq):
    return f"john.q.customer-{seq}"

def get_articles(user, n = 1, paragraphs = 1):
    return articles.get_articles(n, user, paragraphs)
