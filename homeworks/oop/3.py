class DictMixin():
    def to_dict(self):
        return self.__dict__


class Profile(DictMixin):
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex


diana = Profile("Diana", "Tsebenko", "+380975444444", "street Lvivska", 'diana@gmail.com', 'july 6', 17, 'woman')
print(diana.to_dict())
print(f'I am {diana.sex} {diana.name} {diana.last_name} and I am {diana.age}.\nMy birthday is in {diana.birthday}\n'
      f'My phone number and email are {diana.phone_number}, {diana.email}. I live in {diana.address}')
