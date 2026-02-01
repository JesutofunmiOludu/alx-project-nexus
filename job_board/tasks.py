from celery import shared_task
import time

@shared_task
def send_application_notification(application_id, user_email):
    """
    Simulates sending an email notification for a job application.
    In a real app, this would use django.core.mail.
    """
    print(f"Starting notification task for application {application_id}...")
    
    # Simulate a long-running process (like connecting to an SMTP server)
    time.sleep(5)
    
    print(f"Notification sent successfully to {user_email}!")
    return f"Success: Notification sent to {user_email}"
