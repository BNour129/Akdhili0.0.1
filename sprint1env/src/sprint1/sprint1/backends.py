class UrlTokenBackend(ModelBackend):
    def authenticate(self, token):
        try:
            user = User.objects.get(token=token)
        except User.DoesNotExist:
            return None

        if not user.is_active:
            return None

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
