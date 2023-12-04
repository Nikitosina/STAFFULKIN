from models import User
import requests
import json

class API:
    def __init__(self) -> None:
        self.baseUrl = "api/"
    
    def addUser(self, user: User, password: str):
        body = user.__dict__
        body["password"] = password
        j = json.dumps(body)
        response = requests.post(self.baseUrl + "users", json=j)