from django.db.models import Q

from accounts.models import User

from core.filters import AbstractFilterClass

class UserFilterByUsernameAndEmail(AbstractFilterClass):

    def get_filter(self, query):
        return Q(username__contains=query.get('username_email')) \
            | Q(email__contains=query.get('username_email'))

    class Meta:
        model = User


class UserFilter(AbstractFilterClass):

    def get_filter(self, query):
        _filter = Q()
        if query.get('username'):
            _filter &= Q(username__contains=query.get('username'))
        if query.get('email'):
            _filter &= Q(email__contains=query.get('email'))
        if query.get('type_user'):
            _filter &= Q(type_user=query.get('type_user'))        
        return _filter


    class Meta:
        model = User