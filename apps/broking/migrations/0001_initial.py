# Generated by Django 4.2 on 2023-04-25 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('symbol', models.CharField(db_index=True, max_length=40, primary_key=True, serialize=False, unique=True)),
                ('display_name', models.CharField(blank=True, max_length=120, null=True)),
                ('industry_name', models.CharField(blank=True, max_length=120, null=True)),
                ('parent_company', models.CharField(blank=True, max_length=120, null=True)),
                ('nse_script_code', models.CharField(blank=True, max_length=40, null=True)),
                ('is_nse_tradeable', models.BooleanField(default=True)),
                ('bse_script_code', models.CharField(blank=True, max_length=40, null=True)),
                ('is_bse_tradable', models.BooleanField(default=True)),
                ('logo_url', models.ImageField(blank=True, null=True, upload_to='symbol-logos')),
            ],
        ),
    ]
