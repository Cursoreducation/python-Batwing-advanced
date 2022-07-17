
import requests


class ClassForTest:
    def send_request(self):
        response = requests.get("https://company.com")
        return response