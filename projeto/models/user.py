from django.contrib.auth.models import User


def get_full_name(self):
    return '%s %s (%s)' % (self.first_name, self.last_name, self.username)


User.add_to_class("__str__", get_full_name)
