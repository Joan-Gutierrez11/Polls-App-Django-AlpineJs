from django.db.models import Q

from accounts.models import User

from core.filters import AbstractFilterClass

class UserFilterByUsernameAndEmail(AbstractFilterClass):

    def get_filter(self, query):
        return Q(username__contains=query.get('username_email')) \
            | Q(email__contains=query.get('username_email'))

    class Meta:
        model = User
