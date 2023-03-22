import json
from typing import Union

from nbtlib import parse_nbt, serialize_tag
from nbtlib import Compound

class NBT:
    def __init__(self, compound: Union[dict, str, Compound] = "{}"):

        if compound in [None, "", "{}", {}]:
            nbt = None
        elif isinstance(compound, Compound):
            nbt = compound
        elif isinstance(compound, str):
            nbt = json.loads(compound)
        elif isinstance(compound, dict):
            nbt = Compound(compound)
        else:
            raise ValueError(f"Expected dict, str or Compound, got {type(compound)}")

        if nbt:
            for key, value in nbt.items():
                if isinstance(value, Compound):
                    setattr(self, key, NBT(value))
                else:
                    setattr(self, key, value)

    def __setattr__(self, name, value):
        if isinstance(value, NBT):
            super().__setattr__(name, value)
        else:
            nbt = parse_nbt(str({name: value}))
            for key in nbt:
                super().__setattr__(key, nbt[key])

    def __str__(self):
        compound = Compound()

        for key, value in vars(self).items():
            if isinstance(value, NBT):
                compound[key] = Compound(value.__dict__)
            else:
                compound[key] = value

        return serialize_tag(compound, compact=True)