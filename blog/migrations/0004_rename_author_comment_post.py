# Generated by Django 5.1.2 on 2025-01-19 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment", old_name="author", new_name="post",
        ),
    ]
