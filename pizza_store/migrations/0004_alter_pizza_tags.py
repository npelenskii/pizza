# Generated by Django 4.0.3 on 2022-06-06 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_store', '0003_alter_pizza_description_alter_pizza_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='pizza_example_tags', to='pizza_store.tag'),
        ),
    ]
