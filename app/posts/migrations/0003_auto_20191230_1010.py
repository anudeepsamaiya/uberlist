# Generated by Django 3.0.1 on 2019-12-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_auto_20191230_1004"),
    ]

    operations = [
        migrations.CreateModel(
            name="Repost",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name_hash", models.CharField(max_length=32, null=True)),
                ("usr_id", models.CharField(max_length=32, null=True)),
            ],
            options={"abstract": False,},
        ),
        migrations.AddField(
            model_name="postrelation",
            name="re_posts",
            field=models.ManyToManyField(
                related_name="post_relation", to="posts.Repost"
            ),
        ),
    ]
