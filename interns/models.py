from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Tag(models.Model):
    class Meta():
        db_table = "tags"
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Payment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, default=1)
    date = models.DateField()
    sum = models.IntegerField()
    comment = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)




class User(models.Model):
    class Meta:
        db_table = 'intern'
        verbose_name = 'Intern'
        verbose_name_plural = 'Intern'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.IntegerField()
    e_mail = models.EmailField(max_length=50)
    phone = models.IntegerField()  # ???
    city = models.CharField(max_length=20)
    telegram_nickname = models.CharField(max_length=30)
    youtrack_login = models.CharField(max_length=5)  # ???
    edu_lvl = models.CharField(max_length=5)
    edu_university = models.CharField(max_length=5)
    edu_spec = models.CharField(max_length=20)
    resume_title = models.CharField(max_length=20)
    cover_letter_text = models.CharField(max_length=5)  # ???
    skills = models.CharField(max_length=5)  # ???
    skills_detailed = models.CharField(max_length=5)  # ???
    role = models.CharField(max_length=15)
    tags = TaggableManager()


    def __str__(self):
        return str(self.id)


    def get_field_names(self):
        return ['name', 'last_name', 'birth_date', 'e_mail', 'phone', 'tags']


