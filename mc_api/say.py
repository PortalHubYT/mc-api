from mc_api.components import CustomFunction, Message

class Say(CustomFunction):
    def __init__(self, message: Message or str):
        self.check_interface()
        self.message = self.format_arg(message, Message)
    
        self.response = self.send('say', self.message)
        self.status = self.default_check(self.response)

        if self.status is str:
            self.unexpected_status(__file__, self.status, self.command)
            
def say(message: Message or str) -> bool: 
    command = Say(message)
    return command.status

