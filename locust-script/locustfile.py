from locust import HttpUser, task, between
import data
# for clearing the DB on start. readme needs to mention.
import pymongo
import time

class APIUser(HttpUser):
    host = "http://127.0.0.1:4000"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user_data = data.UserData()
        self.user = self.user_data.get_user()
        self.username = self.user["username"]
        self.email = self.user["email"]
        self.password = self.user["password"]

        self.token = "no token"

        # the tasks that this user should run.
        self.list_of_tasks = [
            {"n": 5, "action": self.read_articles},
            self.login,
            lambda : self.post_articles(10),
        ]

    # the only task as far as locust knows
    @task
    def main(self):
        self.execute(self.list_of_tasks)

    # execute a list of tasks in various formats
    # a task can be:
    # - a function
    # - a dict of the form {n, action}
    #   - action can be a callable or a list
    def execute(self, list_of_tasks):
        for task in list_of_tasks:
            if callable(task):
                task()
            elif type(task) == dict:
                n = task["n"]
                action = task["action"]
                for _ in range(n):
                    if type(action) == list:
                        self.execute(action)
                    elif callable(action):
                        action()
                    else:
                        raise Exception("repeaters must be function or list")
            else:
                raise Exception("tasks must be function or dict")

    def post_articles(self, n):
        articles = self.user_data.get_articles(n)
        for article in articles:
            response = self.client.post(
                url = "/api/articles",
                headers = self.make_post_headers(auth = True),
                json = {"article": article}
            )
            self.check(response)

    def read_articles(self):
        self.client.get("/api/articles")

    def make_post_headers(self, auth = False):
        headers = {
            "content-type": "application/json",
            "x-requested-with": "XMLHttpRequest"
            }
        if (auth):
            headers['authorization'] = f'Token {self.token}'
        return headers

    def make_get_headers(self, auth = False):
        headers = {"x-requested-with": "xmlhttprequest"}
        if (auth):
            headers['authorization'] = f'Token {self.token}'
        return headers

    def login(self):
        # don't supply username - that indicates register
        body = {"user": { "email": self.email, "password": self.password}}
        response = self.client.post(
            url = "/api/users/login",
            json = body,
            headers = self.make_post_headers(),
            name = "/api/users/login (login)",
        )
        if response.status_code == 200:
            decoded = response.json()
            self.token = decoded['user']['token']
            if self.username != decoded['user']['username']:
                print(f"mismatched usernames")
            self.username = decoded['user']['username']

        return response

    def register(self):
        body = {"user": {"email": self.email, "password": self.password, "username": self.username}}
        response = self.client.post(
            url = "/api/users",
            json = body,
            headers = self.make_post_headers(),
            name = "/api/users (register)",
        )
        self.check(response)

        decoded = response.json()
        self.token = decoded['user']['token']

        print("got token in register")


    def check(self, response):
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code}")

    def on_start(self):
        mongo_server = "mongodb://127.0.0.1:27017/somedb"

        # use host or env var host (just host for now until determine
        # locust's priorities)
        #
        # clear the existing db so tasks won't fail.
        dbname = mongo_server.split("/")[-1]
        client = pymongo.MongoClient(mongo_server)
        db = client[dbname]

        for collection_name in db.list_collection_names():
            db[collection_name].drop()

        time.sleep(1)

        print(f"on start {self.user}")
        self.register()
