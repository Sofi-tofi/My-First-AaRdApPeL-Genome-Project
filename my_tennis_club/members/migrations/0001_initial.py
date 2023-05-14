# Generated by Django 3.2.12 on 2023-05-14 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=255)),
                ('bioproject', models.CharField(max_length=255)),
                ('biosample', models.CharField(max_length=255)),
                ('assay_type', models.CharField(max_length=255)),
                ('center_name', models.CharField(max_length=255)),
                ('experiment', models.CharField(max_length=255)),
                ('instrument', models.CharField(max_length=255)),
                ('library_layout', models.CharField(max_length=255)),
                ('library_selection', models.CharField(max_length=255)),
                ('library_source', models.CharField(max_length=255)),
                ('org', models.CharField(max_length=255)),
            ],
        ),
    ]