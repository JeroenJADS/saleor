# Generated by Django 2.0.3 on 2018-05-09 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20180405_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='sort_order',
            field=models.PositiveIntegerField(db_index=True, editable=False),
        ),
    ]