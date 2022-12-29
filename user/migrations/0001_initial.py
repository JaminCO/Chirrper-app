# Generated by Django 4.1.2 on 2022-12-29 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('user_name', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('date_registered', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('image_file', models.ImageField(default='default.ico', upload_to='profile_pics')),
                ('bio', models.CharField(default='nothing to see here', max_length=500)),
                ('membership', models.CharField(default='Basic', max_length=20)),
                ('api_token', models.CharField(default='e79f5afc5d4802f667db35d7cfdead5e96d8864bfbea1dc15dfa8ac2b8be025a62be813013abf416a0bc8891e86b8531172418018f889f33bb719e1b2c7d669494d1fc877b1a643f02d402ab46f52e8f30258572226706c5eb8216685216ea6081fce7fe2c4e8186d77296034ed1a47e4e1bddd3e0667caf50b89a01e581ab23c3d19a11a1a0264f3402eaec4102d3b6322a58f345484ab67e72e8effad8bb4b21c8544b2e785c9561070a7872cca738e54076981672346327.2877998', max_length=200, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('content_img', models.ImageField(default='post_default.ico', upload_to='post_pics')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
