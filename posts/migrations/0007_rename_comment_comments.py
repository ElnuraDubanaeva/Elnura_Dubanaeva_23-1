# Generated by Django 4.1.4 on 2022-12-16 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_comment_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Comments',
        ),
    ]
