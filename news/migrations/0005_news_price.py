# Generated by Django 4.2.2 on 2023-06-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_catgory_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]