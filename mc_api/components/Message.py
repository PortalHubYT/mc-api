class Message:
    def __init__(self, message: str):
        """
        Must be a plain text. Can include spaces as well as target 
        selectors. The game replaces entity selectors in the message 
        with the list of selected entities' names, which is formatted 
        as "name1 and name2" for two entities, or 
        "name1, name2, ... and namen" for n entities.
        """
        # TODO: Implement entity selectors handling
        self.message = message

    def __repr__(self):
        return (f'{self.message}')