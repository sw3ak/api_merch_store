# Generated by Django 5.1.6 on 2025-03-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_userprofile_history_received_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='history_received',
            field=models.TextField(default='{}'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='history_sent',
            field=models.TextField(default='{}'),
        ),
    ]
