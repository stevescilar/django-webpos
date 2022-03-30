# Generated by Django 4.0.3 on 2022-03-30 09:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.item', verbose_name='Ordered Item')),
            ],
        ),
    ]
