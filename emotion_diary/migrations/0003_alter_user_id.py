# Generated by Django 4.1.7 on 2023-03-23 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotion_diary', '0002_rename_users_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]