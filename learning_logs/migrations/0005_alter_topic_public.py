# Generated by Django 4.2.3 on 2023-07-27 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_topic_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
