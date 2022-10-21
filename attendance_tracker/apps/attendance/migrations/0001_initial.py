# Generated by Django 4.1.2 on 2022-10-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '__first__'),
        ('student', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(null=True)),
                ('State', models.BooleanField()),
                ('Class_id', models.ManyToManyField(to='classes.classes')),
                ('Student_id', models.ManyToManyField(to='student.student')),
            ],
        ),
    ]