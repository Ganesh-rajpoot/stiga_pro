# Generated by Django 4.2.5 on 2023-09-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_page_abstract_alter_page_full_text_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='abstract',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='page',
            name='full_text_link',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='page',
            name='keywords',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.TextField(max_length=255),
        ),
    ]
