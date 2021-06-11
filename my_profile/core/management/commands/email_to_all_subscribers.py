from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand, CommandError

from core.models import Subscriber


class Command(BaseCommand):
    help = "Email to all of my subscribers"

    def handle(self, *args, **options):
        try:
            from_email = "kan@odds.team"
            subject = "Don't forget to submit your homework :)"
            text_content = "Please submit your homework before Friday!"
            html_content = "<p>Please submit your homework before <strong>Friday</strong>!</p>"

            subscribers = Subscriber.objects.all()
            recipients = [each.email for each in subscribers]

            # See https://github.com/django/django/blob/main/django/core/mail/message.py#L412
            msg = EmailMultiAlternatives(
                subject=subject,
                body=text_content,
                from_email=from_email,
                to=recipients,
                cc=recipients,
                bcc=recipients,
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        except Exception:
            raise CommandError("Error!")
