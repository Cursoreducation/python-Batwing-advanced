class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        profile_list = []
        for value in self.__dict__.values():
            profile_list.append(value)
        return profile_list.__repr__()


man = Profile("Roman", 'Nowicki', 59696868, "Lviv", "bu@mail.com", "5.04.33", 44, "male")
print(man)
