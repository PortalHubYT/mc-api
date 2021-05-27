import re


class NBT:
    def __init__(self, compound: dict = None):

        if isinstance(compound, dict):
            for key in compound:
                setattr(self, key, compound[key])

    def flatten(self, arg):
        if isinstance(arg, dict):
            return str(NBT(arg))
        elif isinstance(arg, str):
            if '"' in arg:
                return f"'{arg}'"
            else:
                return f'"{arg}"'
        elif isinstance(arg, float):
            return f"{arg}d"
        else:
            return arg

    def __str__(self):

        buff = ""

        for key in dir(self):
            if key.startswith("__"):
                continue
            elif key == "flatten":
                continue

            value = getattr(self, key)
            value = self.flatten(value)

            key = re.sub("([a-zA-Z])", lambda x: x.groups()[0].upper(), key, 1)
            buff += f"{key}:{value},"

        if len(buff) > 1 and buff[-1] == ",":
            buff = buff[:-1]

        return f"{{{buff}}}"
