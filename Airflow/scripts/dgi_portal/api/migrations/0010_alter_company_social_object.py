# Generated by Django 4.2.4 on 2023-09-08 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_company_address_alter_company_external_auditor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='social_object',
            field=models.CharField(max_length=10000),
        ),
    ]