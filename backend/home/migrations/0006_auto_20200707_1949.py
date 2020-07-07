# Generated by Django 2.2.14 on 2020-07-07 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_auto_20200707_1849"),
    ]

    operations = [
        migrations.RemoveField(model_name="company", name="actions",),
        migrations.AddField(
            model_name="company",
            name="actions",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="company_actions",
                to="home.Actions",
            ),
        ),
    ]
