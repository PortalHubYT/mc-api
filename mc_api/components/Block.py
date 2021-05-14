class Block:
    def __init__(self, id, namespace="minecraft"):
        self.namespace = namespace
        self.id = id

    def to_str(self):
        return (f'{self.namespace}:{self.id}')