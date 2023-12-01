import json


class User:
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

    def __init__(
        self,
        user_id: str,
        name: str,
        email: str,
        birthdate: str,
        tshirt_size: str,
        education: str,
        university: str,
        soft_skills: [str],
    ) -> None:
        self.id = user_id
        self.name = name
        self.email = email
        self.birthdate = birthdate
        self.tshirt_size = tshirt_size
        self.education = education
        self.university = university
        self.soft_skills = soft_skills
