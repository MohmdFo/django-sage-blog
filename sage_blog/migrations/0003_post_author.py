# Generated by Django 5.1.1 on 2024-10-31 08:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sage_blog", "0002_post_related_posts_post_suggested_posts"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                blank=True,
                db_comment="References the user who authored the post. Can be null if no specific author is assigned.",
                help_text="Select the author of the post.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="posts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Author",
            ),
        ),
    ]