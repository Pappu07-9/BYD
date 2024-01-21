# Generated by Django 5.0.1 on 2024-01-21 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Masterdata',
            fields=[
                ('c_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name_of_customer', models.CharField(default='name', max_length=200)),
                ('address_of_customer', models.CharField(default='address', max_length=200)),
                ('number_of_customer', models.IntegerField(blank=True)),
                ('reference', models.TextField(verbose_name='write a reference')),
                ('interested_model', models.CharField(choices=[('atto 3 advanced', 'Atto 3 Advanced'), ('atto 3 superior', 'Atto 3 Superior'), ('atto 3 premium', 'Atto 3 Premium'), ('dolphin', 'Dolphin'), ('e6', 'E6'), ('m3', 'M3'), ('seal', 'Seal')], max_length=200)),
                ('lead_by', models.CharField(choices=[('generated', 'Generated'), ('walk in', 'walk in')], default='none', max_length=200)),
                ('follow_update', models.DateField()),
                ('status', models.CharField(choices=[('hot', 'Hot'), ('cold', 'Cold'), ('warm', 'Warm')], default='warm', max_length=200)),
                ('book_status', models.BooleanField(default=False)),
                ('test_drive', models.BooleanField(default=False)),
            ],
        ),
    ]