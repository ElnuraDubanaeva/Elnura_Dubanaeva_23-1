# Generated by Django 4.1.4 on 2022-12-29 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_product_author_review_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='title',
        ),
    ]