# Generated by Django 4.0.2 on 2022-04-05 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plants',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.kind'),
        ),
        migrations.AlterField(
            model_name='plants',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.type'),
        ),
    ]
