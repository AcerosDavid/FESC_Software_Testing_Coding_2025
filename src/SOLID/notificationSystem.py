from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str) -> None:
        pass


class EmailNotification(NotificationSender):
    def send(self, message: str, recipient: str) -> None:
        print(f"📧 Sending Email to {recipient}: {message}")


class SMSNotification(NotificationSender):
    def send(self, message: str, recipient: str) -> None:
        print(f"📱 Sending SMS to {recipient}: {message}")


class PushNotification(NotificationSender):
    def send(self, message: str, recipient: str) -> None:
        print(f"🔔 Sending Push Notification to {recipient}: {message}")


class NotificationService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def notify(self, message: str, recipient: str) -> None:
        self.sender.send(message, recipient)


# Usage example
if __name__ == "__main__":
    email_sender = NotificationService(EmailNotification())
    sms_sender = NotificationService(SMSNotification())
    push_sender = NotificationService(PushNotification())

    email_sender.notify("Welcome to the system", "user@email.com")
    sms_sender.notify("Your code is 1234", "+1234567890")
    push_sender.notify("You have a new pending task", "app_user")
