from abc import ABC, abstractmethod


# Defined an interface for Payment Processors
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


# Concrete Implementations
class EmailNotification(Notification):
    def send(self, message: str):
        return f"Sending Email with message: {message}"


class SMSNotification(Notification):
    def send(self, message: str):
        return f"Sending SMS with message: {message}"


class PushNotification(Notification):
    def send(self, message: str):
        return f"Sending Push Notification with message: {message}"


# Factory Class
class NotificationFactory:
    @staticmethod
    def create_notification(channel: str) -> Notification:
        if channel.lower() == "email":
            return EmailNotification()
        elif channel.lower() == "sms":
            return SMSNotification()
        elif channel.lower() == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification channel: {channel}")


# Client Code
def main():
    factory = NotificationFactory()
    email_notification = factory.create_notification("email")
    print(email_notification.send("email"))

    try:
        unknown_notification = factory.create_notification('fax')
        print(unknown_notification.send("This is from Fax :)"))
    except Exception as e:
        print(e)


# Running main function
if __name__ == "__main__":
    main()
