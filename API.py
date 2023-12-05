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
        # response = requests.post(self.baseUrl + "users", json=j)

    def getUser(self, id: str) -> User:
        sample = json.loads(
            """{
                "user_id": "iivanov",
                "name": "Иван Иванов",
                "email": "iivanov@example.com",
                "birthdate": "1990-01-01",
                "tshirt_size": "M",
                "education": "Высшее образование",
                "university": "Университет",
                "soft_skills": [
                    "Коммуникабельность",
                    "Организованность"
                ]
            }"""
        )
        return User(**sample)
