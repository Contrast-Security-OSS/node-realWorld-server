from locust import HttpUser, task, between
import json

class APIUser(HttpUser):
    host = "http://127.0.0.1:4000"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_of_tasks = [
            {"n": 5, "fn_or_list": self.read_articles},
            self.login,
            self.simple_post_and_read,
        ]

    @task
    def main(self):
        self.execute(self.list_of_tasks)

    def execute(self, list_of_tasks):
        for task in list_of_tasks:
            if callable(task):
                task()
            elif type(task) == dict:
                n = task["n"]
                fn_or_list = task["fn_or_list"]
                for _ in range(n):
                    if type(fn_or_list) == list:
                        self.execute(fn_or_list)
                    elif callable(fn_or_list):
                        fn_or_list()
                    else:
                        raise Exception("repeaters must be function or list")
            else:
                raise Exception("tasks must be function or dict")

    #@task
    def simple_post_and_read(self):
        # status = self.login()
        # if status == 200:
        #     print("login succeeded")
        # else:
        #     print("login failed")

        response = self.client.get("/api/articles")

        response = self.client.get(
            url = "/api/articles",
            headers = self.make_get_headers(auth = True)
        )
        body = {
            "article":{
                "title":"How to train your cat",
                "description":"Ever wonder how?",
                "body":"Let your cat train you instead; it is much easier.",
                "tagList":["training", "cats"]
                }
            }
        print(self.make_post_headers(auth = True))
        response = self.client.post(
            url = "/api/articles",
            headers = self.make_post_headers(auth = True),
            json = body
        )
        #print(response.json())

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

    # @task(3)
    # def view_items(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)

    def login(self):
        # need to fetch multiple from some source
        email = "bruce@bruce.com"
        password = "giggles75"
        # not used for login, if present, it's "register"
        #username = "bruce"
        body = {"user": { "email": email, "password": password}}
        response = self.client.post(
            url = "/api/users/login",
            json = body,
            headers = self.make_post_headers(),
            name = "/api/users/login (login)",
        )
        if response.status_code == 200:
            decoded = response.json()
            self.token = decoded['user']['token']

        return response

    def register(self):
        # need to fetch multiple from some source
        email = "bruce-again@bruce.com"
        password = "giggles75"
        username = "bruce-again"
        body = {"user": { "email": email, "password": password, "username": username}}
        response = self.client.post(
            url = "/api/users/login",
            json = body,
            headers = self.make_post_headers(),
            name = "/api/users/login (login)",
        )
        if response.status_code == 200:
            decoded = response.json()
            self.token = decoded['user']['token']

    def on_start(self):
        print("on_start")
        # APIUser.list_of_tasks.append({"n": 5, "fn_or_list": self.read_articles})
        # APIUser.list_of_tasks.append(self.simple_post_and_read)

    # def on_start(self):
    #     EMAIL = "bruce@bruce.com"
    #     PASSWORD = "giggles75"
    #     USERNAME = "bruce-x"
    #     # "{\"user\":{\"email\":\"{{EMAIL}}\", \"password\":\"{{PASSWORD}}\", \"username\":\"{{USERNAME}}\"}}"
    #     json = {"user": { "email": EMAIL, "password": PASSWORD, "username": USERNAME }}
    #     response = self.client.post(
    #         url="/api/users/login",
    #         json=json,
    #         headers={"content-type": "application/json", "x-requested-with": 'XMLHttpRequest'},
    #         #name="login" # no name defaults to url
    #         )
    #     response = response.json()
    #     self.token = response['user']['token']
    #     print(response)

    # notes:
    # on start:
    #   register users? or clear DB?
    #   how to clear DB if not. or force restart after deleting DB?
    #   or start DB with known users?
    # each task:
    #   login
    #   post articles (n, vary sizes, etc)
    #
