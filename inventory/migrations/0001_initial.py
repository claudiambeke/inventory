# Generated by Django 3.2.9 on 2021-11-21 22:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='inventory.basemodel')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('store_name', models.TextField()),
                ('user_uuid', models.UUIDField()),
                ('location_uuid', models.UUIDField()),
            ],
            bases=('inventory.basemodel',),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='inventory.basemodel')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.TextField()),
                ('price', models.TextField()),
                ('quantity', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('store_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.stores')),
            ],
            bases=('inventory.basemodel',),
        ),
    ]