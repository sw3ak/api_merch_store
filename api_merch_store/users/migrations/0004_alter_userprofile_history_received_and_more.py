# Generated by Django 5.1.6 on 2025-03-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_history_received_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='history_received',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='history_sent',
            field=models.JSONField(default=list),
        ),
    ]
