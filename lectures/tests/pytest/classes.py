import requests


class ClassForTest:
    def send_request(self):
        response = requests.get("https://jsonplaceholder.typicode.com/todosasdasdsadsada")
        return response
