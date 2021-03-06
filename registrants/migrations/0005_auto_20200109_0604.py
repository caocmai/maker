# Generated by Django 3.0.2 on 2020-01-09 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registrants', '0004_auto_20200108_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Non-Binary')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(help_text='Enter the city', max_length=30),
        ),
        migrations.CreateModel(
            name='Complement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=160)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('to_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrants.UserProfile')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
