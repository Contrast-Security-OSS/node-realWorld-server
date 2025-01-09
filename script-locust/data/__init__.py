import data.articles as articles

class UserData:
    _user_seq = 0

    def __init__(self):
        self._article_seq = 0

        UserData._user_seq += 1
        self._user_seq = f"{UserData._user_seq:02d}"

        self.username = self.make_username()
        self.email = self.make_email()
        self.password = "password-might-be-long-enough"

    def get_user(self):
        return {
            "email": self.email,
            "password": "password-might-be-long-enough",
            "username": self.username,
        }

    def make_email(self):
        return f"{self.make_username()}@abysmal.com"

    def make_username(self, name = "john.q.customer"):
        return f"{name}-{self._user_seq}"

    def get_articles(self, n = 1, paragraphs = 1):
        unique_articles = articles.get_articles(n, paragraphs)
        # make the title unique by combining user and user-specific sequence
        for article in unique_articles:
            self._article_seq += 1
            title = article["title"]
            article["title"] = f"{title} by {self.username} ({self._article_seq})"

        return unique_articles
