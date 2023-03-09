from django.db import models

# Create your models here.

class SafeDeleteAbstractClass(models.Model):
    """
    Abstract class that defined the safe delete in database.
    Needs set the STATUS_FIELD
    """

    STATUS_FIELD = None

    def _check_errors(self):
        if not self.__getattribute__('STATUS_FIELD') or \
            self.__getattribute__('STATUS_FIELD') == '':
            raise NotImplementedError('This class not indicate the status field')

        if not self.__getattribute__('pk'):
            raise TypeError("This object hadn't save in database")

    def safe_delete(self):
        self._check_errors()
        self.__setattr__(self.STATUS_FIELD, False)
        self.save()

    def restore(self):
        self._check_errors()
        self.__setattr__(self.STATUS_FIELD, True)
        self.save()
    
    class Meta:
        abstract = True

class SafeDeleteModel(SafeDeleteAbstractClass):
    active = models.BooleanField(null=False, default=True)

    STATUS_FIELD = 'active'

    class Meta:
        abstract = True
