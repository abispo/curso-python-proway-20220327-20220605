# Generated by Django 4.0.4 on 2022-06-05 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_account', '0002_financialaccount_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialaccount',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
