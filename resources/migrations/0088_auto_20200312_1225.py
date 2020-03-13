# Generated by Django 2.2.10 on 2020-03-12 10:25

from django.db import migrations


def copy_templates(apps, schema_editor):
    OldNotificationTemplate = apps.get_model('notifications', 'NotificationTemplate')
    NotificationTemplate = apps.get_model('django_ilmoitin', 'NotificationTemplate')
    all_notification_templates = OldNotificationTemplate.objects.all()

    for old_tmpl in OldNotificationTemplate.objects.language('fi').all():
        new_tmpl = NotificationTemplate()
        new_tmpl.type = old_tmpl.type

        new_tmpl.set_current_language('fi')
        new_tmpl.subject = old_tmpl.subject
        new_tmpl.body_text = old_tmpl.body
        new_tmpl.body_html = old_tmpl.html_body
        new_tmpl.save()

class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0087_add_payment_terms'),
        ('notifications', '0005_add_access_code_created_notification')
    ]

    operations = [
        migrations.RunPython(copy_templates),
    ]
