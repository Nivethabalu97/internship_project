# Generated by Django 4.1.6 on 2023-02-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_emp_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='emp_roll',
            field=models.IntegerField(null=True),
        ),
    ]
