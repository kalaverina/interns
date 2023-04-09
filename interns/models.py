from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    #user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.IntegerField()
    e_mail = models.EmailField(max_length=50)
    phone = models.IntegerField()
    city = models.CharField(max_length=5)
    telegram_nickname = models.CharField(max_length=5)
    youtrack_login = models.CharField(max_length=5)
    edu_lvl = models.CharField(max_length=5)
    edu_institut = models.CharField(max_length=5)
    edu_spec = models.CharField(max_length=5)
    resume_title = models.CharField(max_length=5)
    cover_letter_text = models.CharField(max_length=5)
    skills = models.CharField(max_length=5)
    skills_detailed = models.CharField(max_length=5)
    role = models.CharField(max_length=5)

    def __str__(self):
        return str(self.id)

    def get_field_names(self):
        return [field.name for field in self._meta.fields]


class Payment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, default=1)
    date = models.DateField()
    sum = models.IntegerField()
    comment = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)


class Tags(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=5)
    comment = models.CharField(max_length=5)

    def __str__(self):
        return str(self.id)


class UserTags(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    tag_id = models.OneToOneField('Tags', on_delete=models.CASCADE)

