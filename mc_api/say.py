from mc_api.components import Message
from .base_functions import *

def _say(message: Message) -> bool:
    response = send('say', message)
    status = default_check(response)

    if status is str:
        unexpected_status(__file__, status)

    return status

def say(message: Message or str) -> bool:
    check_output_channel()
    
    message = format_arg(message, Message)

    return _say(message)