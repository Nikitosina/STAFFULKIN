class User:
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

    @classmethod
    def fromForm(cls, form):
        username = form.get("username")
        email = form.get("email")
        birthdate = form.get("birthdate")
        tshirt_size = form.get("tshirt_size")
        education = form.get("education")
        university = form.get("university")
        position = form.get("position")
        return cls(
            user_id="",
            name=username,
            email=email,
            birthdate=birthdate,
            tshirt_size=tshirt_size,
            education=education,
            university=university,
            soft_skills=[],
        )
