class NBTTags:
    def __init__(self):
        self.tags = {}

    def add(self, property, value):
        self.tags[property] = value

    def __repr__(self):
        print(self.tags)
        return None
        return(f'{self.value}')

metadata = NBTTags()
metadata.add('Invincible', '1')