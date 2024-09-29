
_user_seq = 0

def _useq():
    global _user_seq
    _user_seq += 1
    return f"{_user_seq:03d}"

import data.articles as articles

def get_user():
    seq = _useq()
    return {
        "email": make_email(seq),
        "password": "password",
        "username": make_username(seq),
    }

def make_email(seq):
    return f"john.q.customer-{seq}@abysmal.com"

def make_username(seq):
    return f"john.q.customer-{seq}"

_article_seq = 0

def _aseq():
    global _article_seq
    _article_seq += 1
    return f"{_article_seq:03d}"

def get_articles(user, n = 1, paragraphs = 1):
    # this assures that each article has a unique title (slug). the bodies
    # don't need to be unique.
    combined_seq = f"{user}-{_aseq()}"
    return articles.get_articles(n, combined_seq, paragraphs)
