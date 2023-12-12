import json

text = """{'company_tree': {'employeeId': 1, 'employeeName': 'CEO', 'subordinates': [{'employeeId': 2, 'employeeName': 'Manager 1', 'subordinates': [{'employeeId': 4, 'employeeName': 'Employee 1', 'subordinates': []}, {'employeeId': 5, 'employeeName': 'Employee 2', 'subordinates': []}]}, {'employeeId': 3, 'employeeName': 'Manager 2', 'subordinates': [{'employeeId': 6, 'employeeName': 'Employee 3', 'subordinates': []}]}]}}"""
text = text.replace("'", '"')
j = json.loads(text)


class TreeEntry:
    def __init__(self, employeeId: int, employeeName: str, subordinates) -> None:
        self.employee_id = employeeId
        self.employee_name = employeeName
        self.subordinates = subordinates


def parse_json(j) -> TreeEntry:
    # for k, v in json.items():
    if len(j["subordinates"]) == 0:
        return TreeEntry(**j)

    children = []
    for subordinate in j["subordinates"]:
        children.append(parse_json(subordinate))

    return TreeEntry(
        employeeId=j["employeeId"],
        employeeName=j["employeeName"],
        subordinates=children,
    )


tree = parse_json(j["company_tree"])
print(tree)
