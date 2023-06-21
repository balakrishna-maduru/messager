from messager.sender import Sender


def lambda_handler(event, context):
    print("Started execution")
    sender = Sender()
    return sender.send()
