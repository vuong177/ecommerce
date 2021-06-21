# Generated by Django 2.2.14 on 2021-05-26 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0004_auto_20210526_0723'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_ID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('creation_date', models.DateField(auto_now=True)),
                ('is_end', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('address1', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=11)),
                ('products', models.ManyToManyField(to='home.Product')),
                ('seller_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-creation_date',),
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('products', models.ManyToManyField(to='home.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Customer')),
            ],
        ),
    ]
