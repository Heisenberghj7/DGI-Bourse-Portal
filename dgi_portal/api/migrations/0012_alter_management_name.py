# Generated by Django 4.2.4 on 2023-09-09 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_management_name_alter_management_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management',
            name='name',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
