class UserDB:
    users = [{"name": "test", "email": "test@test.com", "password": "passhash"}]

    def get_all(self):
        return self.users

    def retrieve_by_email(self, email):
        for user in self.users:
            if user["email"] == email:
                return user
        return None

    def add(self, user):
        # add check if user already exists
        user = {
            "name": user.get('name'),
            "email": user.get('email'),
            "password": user.get('password')
        }
        self.users.append(user)
        return user

    def update_by_email(self, email, name, password):
        # TODO: refactor
        for user in self.users:
            if user["email"] == email:
                user["name"] = name
                user["password"] = password
                return user
        return None

    def delete_by_email(self, email):
        self.users = [user for user in self.users if user["email"] != email]
