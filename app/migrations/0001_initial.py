# Generated by Django 4.1.3 on 2022-11-26 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=55)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[("boshlang'ich", 'Begin'), ("o'ratacha", 'Middle'), ('yuqori', 'Hight')], default="boshlang'ich", max_length=25)),
                ('image', models.ImageField(upload_to='images/')),
                ('first_name', models.CharField(max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('birth_day', models.CharField(max_length=10)),
                ('course_name', models.CharField(choices=[('Dasturlash', 'Course1'), ('Koreys tili', 'Course2')], default='Dasturlash', max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('telegram', models.CharField(max_length=80)),
                ('prietice', models.IntegerField(choices=[('1-3', 'Three Years'), ('3-5', 'Five Years'), ('5+', 'Five Pulse')], default='1-3')),
                ('university', models.CharField(max_length=55)),
                ('language', models.CharField(choices=[("O'zbek", 'Uzbek'), ('Rus', 'Rus'), ('Turk', 'Turk'), ('Nemis', 'Nemis'), ('Ingiliz', 'Ingiliz'), ('Koryes', 'Koryes')], default="O'zbek", max_length=30)),
                ('price', models.IntegerField(choices=[('100000', 'Yuzming'), ('200000', 'Two Hundred Thousand'), ('300000', 'Three Hundred Thousand')], default='100000')),
                ('resyume_file', models.FileField(upload_to='')),
                ('serficate_file', models.FileField(upload_to='')),
                ('about_from', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=40)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Complaiut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
