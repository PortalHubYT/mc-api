from .TargetSelector import TargetSelector


class Message:
    def __init__(self, *args):
        """
        Must be a plain text. Can include spaces as well as target
        selectors. The game replaces entity selectors in the message
        with the list of selected entities' names, which is formatted
        as "name1 and name2" for two entities, or
        "name1, name2, ... and namen" for n entities.
        """

        self.args = args

    def __str__(self):
        buff = ""

        for argument in self.args:

            if not isinstance(argument, str) and not isinstance(
                argument, TargetSelector
            ):
                raise ValueError(
                    f"A Message must be composed exclusively of string and eventually TargetSelector instances"
                )
            elif isinstance(argument, str):
                buff += argument + " "
            else:
                buff += str(argument) + " "

        if len(buff) > 1 and buff[-1] == " ":
            buff = buff[:-1]

        return f"{buff}"
