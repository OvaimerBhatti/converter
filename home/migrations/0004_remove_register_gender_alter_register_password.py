# Generated by Django 4.0.4 on 2022-05-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_register_email_alter_register_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='gender',
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]