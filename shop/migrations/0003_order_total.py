# Generated by Django 3.2.8 on 2021-11-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
