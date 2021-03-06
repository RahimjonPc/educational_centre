# Generated by Django 3.1.5 on 2021-01-12 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='teacher_poster')),
                ('bio', models.CharField(max_length=250)),
                ('experience', models.CharField(max_length=250)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.DateField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='student_poster')),
                ('sex', models.CharField(max_length=10)),
                ('age', models.DateField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaderProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='leader_poster')),
                ('sex', models.CharField(blank=True, max_length=10)),
                ('age', models.DateField(blank=True)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
