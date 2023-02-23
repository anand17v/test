# Generated by Django 1.11.16 on 2019-01-10 09:19


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verify_student', '0010_manualverification'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwaresecurephotoverification',
            name='expiry_date',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='softwaresecurephotoverification',
            name='expiry_email_date',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]