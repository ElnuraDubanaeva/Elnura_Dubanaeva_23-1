# Generated by Django 4.1.4 on 2022-12-23 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_hashtag_product_hashtags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hashtag',
            new_name='Categories',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='hashtags',
            new_name='categories',
        ),
    ]