# Generated by Django 4.2.2 on 2023-07-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_costumer_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="costumer",
            name="profile_pic",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]