# Generated by Django 4.2 on 2023-05-10 05:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_comment_created_date_alter_post_create_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="created_date",
        ),
        migrations.AddField(
            model_name="comment",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 10, 5, 28, 9, 839538, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 10, 5, 28, 9, 838549, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
