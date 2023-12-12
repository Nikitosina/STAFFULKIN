class Goal:
    def __init__(self, name: str, description: str, deadline: str) -> None:
        self.name = name
        self.description = description
        self.deadline = deadline

    @classmethod
    def fromForm(cls, form):
        name = form.get("name")
        description = form.get("description")
        deadline = form.get("deadline")
        return Goal(name=name, description=description, deadline=deadline)


class User:
    def __init__(
        self,
        user_id: str,
        name: str,
        email: str,
        status: str,
        phone_number: str,
        team: str,
        birthdate: str,
        tshirt_size: str,
        education: str,
        university: str,
        soft_skills: [str],
        boss_id: int = 0,
        goals: [Goal] = [],
        calendar_events: [any] = [],
        position: str = "",
    ) -> None:
        self.id = user_id
        self.name = name
        self.email = email
        self.status = status
        self.phone_number = phone_number
        self.team = team
        self.birthdate = birthdate
        self.tshirt_size = tshirt_size
        self.education = education
        self.university = university
        self.soft_skills = soft_skills
        self.boss_id = boss_id
        self.goals = goals
        self.calendar_events = calendar_events
        self.postion = position

    @classmethod
    def fromForm(cls, form):
        username = form.get("username")
        email = form.get("email")
        phone = form.get("phone")
        birthdate = form.get("birthdate")
        tshirt_size = form.get("tshirt_size")
        education = form.get("education")
        university = form.get("university")
        position = form.get("position")
        return cls(
            user_id="",
            name=username,
            email=email,
            phone_number=phone,
            birthdate=birthdate,
            tshirt_size=tshirt_size,
            education=education,
            university=university,
            position=position,
            soft_skills=[],
            status="В сети",
            team="Great team",
        )


class TreeEntry:
    def __init__(self, employeeId: int, employeeName: str, subordinates) -> None:
        self.employee_id = employeeId
        self.employee_name = employeeName
        self.subordinates = subordinates
