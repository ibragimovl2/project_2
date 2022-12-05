from django.db import models
from django.db.models import TextChoices


class User(models.Model):
    class StatusChoice(TextChoices):
        BEGIN = 'boshlang\'ich'
        MIDDLE = 'o\'ratacha'
        HIGHT = 'yuqori'

    status = models.CharField(max_length=25, choices=StatusChoice.choices, default=StatusChoice.BEGIN)
    image = models.ImageField(upload_to='images/')
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    birth_day = models.CharField(max_length=10)

    class Course_nameChoice(TextChoices):
        course1 = 'Dasturlash'
        course2 = 'Koreys tili'

    course_name = models.CharField(max_length=30, choices=Course_nameChoice.choices, default=Course_nameChoice.course1)
    email = models.EmailField()
    phone_number = models.IntegerField()
    telegram = models.CharField(max_length=80)



    class PrieticeChoice(TextChoices):
        three_years = '1-3'
        five_years = '3-5'
        five_pulse = '5+'

    prietice = models.IntegerField(choices=PrieticeChoice.choices, default=PrieticeChoice.three_years)
    university = models.CharField(max_length=55)

    class LanguageChoice(TextChoices):
        uzbek = 'O\'zbek'
        rus = 'Rus'
        turk = 'Turk'
        nemis = 'Nemis'
        ingiliz = 'Ingiliz'
        koryes = 'Koryes'

    language = models.CharField(max_length=30, choices=LanguageChoice.choices, default=LanguageChoice.uzbek)

    class PriceChoice(TextChoices):
        yuzming = '100000'
        two_hundred_thousand = '200000'
        three_hundred_thousand = '300000'

    price = models.IntegerField(choices=PriceChoice.choices, default=PriceChoice.yuzming)
    resyume_file = models.FileField()
    serficate_file = models.FileField()
    about_from = models.TextField()


class Course(models.Model):
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name


class Complaiut(models.Model):
    title = models.CharField(max_length=55)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=55)
    comment = models.TextField()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

class Home(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=55)
    text = models.TextField()
    languages = models.CharField(max_length=55)
    items = models.CharField(max_length=55)
    it_texnolog = models.CharField(max_length=55)


class Post(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField()
    buy_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name