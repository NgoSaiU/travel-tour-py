# Generated by Django 4.2.7 on 2023-12-03 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0009_booking_active_comment_active_news_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.CharField(max_length=10),
        ),
    ]
