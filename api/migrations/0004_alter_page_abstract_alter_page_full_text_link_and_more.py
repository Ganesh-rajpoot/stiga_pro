# Generated by Django 4.2.5 on 2023-09-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_abtract_page_abstract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='abstract',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='page',
            name='full_text_link',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='page',
            name='keywords',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.TextField(max_length=10000),
        ),
    ]
