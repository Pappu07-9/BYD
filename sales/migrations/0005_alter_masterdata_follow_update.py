# Generated by Django 5.0.1 on 2024-01-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_alter_masterdata_follow_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterdata',
            name='follow_update',
            field=models.DateField(auto_now=True),
        ),
    ]