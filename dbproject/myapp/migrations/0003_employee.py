# Generated by Django 4.1.5 on 2023-02-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_student_age_student_marks_student_name_student_stype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('age', models.IntegerField(null=True)),
                ('position', models.CharField(max_length=50)),
                ('years', models.IntegerField(default=True)),
            ],
        ),
    ]
