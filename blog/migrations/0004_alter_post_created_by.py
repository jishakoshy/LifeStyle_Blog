# Generated by Django 5.0.7 on 2024-07-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_categories_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_by',
            field=models.DateTimeField(),
        ),
    ]
