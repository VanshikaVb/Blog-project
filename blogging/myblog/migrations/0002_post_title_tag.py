# Generated by Django 4.2.6 on 2023-10-25 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myblog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="title_tag",
            field=models.CharField(default="My blogging site!", max_length=255),
        ),
    ]
