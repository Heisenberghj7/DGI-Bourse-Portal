# Generated by Django 4.2.4 on 2023-09-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_contact_fax_alter_contact_mail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dividend',
            name='amount',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='dividend',
            name='dividend_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='dividend',
            name='year',
            field=models.CharField(default='', max_length=100),
        ),
    ]
