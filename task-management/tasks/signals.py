from django.db.models.signals import m2m_changed, post_delete
from django.dispatch import receiver
from .models import Task
from django.core.mail import send_mail
from django.conf import settings

@receiver(m2m_changed, sender=Task.assigned_to.through)
def notyfy_task_creation(sender, instance, action, **kwargs):
    if action == 'post_add':
        assigned_emails = [user.email for user in instance.assigned_to.all()]
        send_mail(
            'Task Assignment',
            f'The task "{instance.title}" has been assigned to you.',
            settings.EMAIL_HOST_USER,
            assigned_emails,
            fail_silently=False
        )

# @receiver(post_delete, sender=Task)
# def delete_associated_details(sender, instance, **kwargs):
#     if instance.details:
#         instance.details.delete()