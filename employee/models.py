from django.db import models
# Create your models here.

class EmployeeData(models.Model):
    emp_no = models.IntegerField(_('employee number'), primary_key=True)
    first_name = models.CharField(_('first name'), max_length=14)
    last_name = models.CharField(_('last name'), max_length=16)
    gender = models.CharField(_('gender'), max_length=1)
    birth_date = models.DateField(_('birthday'))
    address = models.TextField(_("address"))
    hire_date = models.DateField(_('hire date'))

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)