# Generated by Django 3.2.5 on 2021-07-31 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='email',
            field=models.EmailField(blank=True, help_text='Use the following email format example@gmail.com', max_length=254),
        ),
    ]
