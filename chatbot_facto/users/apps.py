from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "chatbot_facto.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import chatbot_facto.users.signals  # noqa F401
        except ImportError:
            pass
