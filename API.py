from models import User, Goal, TreeEntry
from flask import session
import requests
import json
from constants import ACCESS_TOKEN_KEY


class APIError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class API:
    def __init__(self) -> None:
        self.baseUrl = "http://84.252.143.140/api/"

    def authorizeIfNeeded(self, session: session, username: str, password: str) -> str:
        headers = {"accept": "*/*", "Content-Type": "application/json"}
        body = {"email": username, "password": password}
        response: requests.Response = requests.post(
            self.baseUrl + "auth/token", headers=headers, data=json.dumps(body)
        )
        check_response(response=response)

        d = json.loads(response.text)
        session[ACCESS_TOKEN_KEY] = d[ACCESS_TOKEN_KEY]
        print(d)
        return d["userId"]

    def addUser(self, user: User, access_token: str) -> str:
        body = json.dumps(user.__dict__)
        response = requests.post(
            self.baseUrl + "users",
            data=body,
            headers=default_header(access_token=access_token),
        )
        check_response(response=response)
        j = json.loads(response.text)
        print(j)
        return j["user_id"]

    def getCompanyTree(self, access_token: str) -> TreeEntry:
        response = requests.get(
            self.baseUrl + "company/tree",
            headers=default_header(access_token=access_token),
        )
        check_response(response=response)
        j = json.loads(response.text)
        tree = parse_tree(j["company_tree"])
        return tree

    def getUser(self, id: str, access_token: str) -> User:
        response: requests.Response = requests.get(
            self.baseUrl + f"users/{id}",
            headers=default_header(access_token=access_token),
        )
        check_response(response=response)
        d = json.loads(response.text)
        return User(**d)

    def addGoal(self, user_id: str, goal: Goal, access_token: str):
        body = json.dumps(goal.__dict__)
        response = requests.post(
            self.baseUrl + f"goals?employee_id={user_id}",
            data=body,
            headers=default_header(access_token=access_token),
        )
        check_response(response=response)


def default_header(access_token: str) -> dict[str, str]:
    headers = {"accept": "*/*", "Content-Type": "application/json"}
    if access_token != None:
        headers["Authorization"] = f"Bearer {access_token}"

    return headers


def check_response(response: requests.Response):
    if response.status_code == 200:
        return
    elif response.status_code == 401:
        raise APIError("Not authorized")
    else:
        raise APIError(f"Bad status code: {response.status_code}")


def parse_tree(j) -> TreeEntry:
    if len(j["subordinates"]) == 0:
        return TreeEntry(**j)

    children = []
    for subordinate in j["subordinates"]:
        children.append(parse_tree(subordinate))

    return TreeEntry(
        employeeId=j["employeeId"],
        employeeName=j["employeeName"],
        subordinates=children,
    )
