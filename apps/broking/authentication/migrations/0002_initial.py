# Generated by Django 4.2 on 2023-04-25 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authsession',
            name='app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.tradeapp'),
        ),
        migrations.AddField(
            model_name='authsession',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
