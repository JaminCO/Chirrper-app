# Generated by Django 4.1.4 on 2024-01-23 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_platform', '0010_alter_post_draft'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='body',
        ),
    ]
