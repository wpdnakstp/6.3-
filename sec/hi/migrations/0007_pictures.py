# Generated by Django 2.2.1 on 2019-06-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hi', '0006_choice_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='blogimg')),
            ],
        ),
    ]
