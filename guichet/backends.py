from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EtudiantBackend(ModelBackend):
    def authenticate(self, request, cne=None, cin=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(cne=cne, cin=cin)
        except User.DoesNotExist:
            return None
        else:
            return user if self.user_can_authenticate(user) else None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
