from mcstacker_data import get_entity_nbt_json
from minecraft_data import JarParser

# This is hacky right now and needs to fit with the filename
# of the mcstacker .js files we're downloading

SHULKER_VERSION = '1.19.4'

# This parses the server.jar files and generates the .json files
# that we'll use for Shulker
jar_parsing = JarParser(SHULKER_VERSION, verbose=True)
jar_parsing.run()

# This creates the entity_nbt.json file from the data generated, and from
# mcstacker's website source code
get_entity_nbt_json()
