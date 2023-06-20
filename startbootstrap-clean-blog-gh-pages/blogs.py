import requests


class Blog:
    def __init__(self):
        self.response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        self.data = self.response.json()

    def first_blog(self):
        blog = self.data[0]
        return blog

    def second_blog(self):
        blog = self.data[1]
        return blog

    def third_blog(self):
        blog = self.data[2]
        return blog




