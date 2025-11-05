class UserService:
    def authenticate(self, username, password):
        return f"Аутентификация пользователя {username}"

    def get_user_profile(self, user_id):
        return f"Профиль пользователя {user_id}"