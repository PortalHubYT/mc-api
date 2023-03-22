import json
import logging
import re
import os
import html

import jsbeautifier
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

"""This .py files depends on registries.json that is extracted from a server.jar file.
There are utilities in the ./setup folder that can be used to extract the registries.json file.
"""

path = os.path.dirname(os.path.abspath(__file__))

def get_mcstacker_driver():
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    # Create a new instance of the Firefox driver service
    logging.info("Creating a new Firefox driver service")
    geckodriver_path = '/usr/local/bin/geckodriver'
    firefox_service = FirefoxService(executable_path=geckodriver_path)

    # Create a new instance of the Firefox driver
    logging.info("Creating a new Firefox driver instance")
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options, service=firefox_service)

    # Navigate to the website where you want to execute the JavaScript function
    logging.info("Navigating to the website")
    driver.get("https://mcstacker.net/")
    
    return driver

def clean_driver(driver):
    # Close the browser window
    logging.info("Closing the browser window")
    driver.quit()
    
    # Delete the geckodriver.log file
    try:
        os.remove("geckodriver.log")
    except:
        pass
    
def get_entity_list():
    # First we open the registries.json and load the key 'minecraft:entity_type' into a variable
    with open(f'{path}/data/registries.json') as f:
        registries = json.load(f)
        entity_type = registries['minecraft:entity_type']

    # We create a list out of all the keys in the entity_type dictionary
    entities = list(entity_type['entries'].keys())

    # For each entity we remove the 'minecraft:' part
    entities = [entity.replace('minecraft:', '') for entity in entities]

    return entities

def get_entity_data(entities):
    
    driver = get_mcstacker_driver()
    
    entity_nbt = {}
    
    for entity in entities:
        logging.info("Executing the JavaScript function")
        result = driver.execute_script(f'return loadEntityClass("{entity}", "0");')
        
        logging.info(f"Result: {result}")
        entity_nbt[entity] = result

    with open(f'{path}/data/entity_nbt.json', 'w') as f:
        f.write(json.dumps(entity_nbt, indent=4))
        
    clean_driver(driver)

def reformat_entity_nbt():
    with open(f'{path}/data/entity_nbt.json') as f:
        entity_nbt = json.load(f)

    new_entity_nbt = {}
    
    for entity in entity_nbt:
        
        if entity_nbt[entity] is None:
            continue
        
        new_entity_nbt[entity] = {}
        
        for key in entity_nbt[entity]:
            if key.endswith('NBT'):
                new_entity_nbt[entity].update(entity_nbt[entity][key])
            elif key != 'stackPos':
                new_entity_nbt[entity][key] = entity_nbt[entity][key]
    
    even_newer_entity_nbt = {}
    
    for entity in new_entity_nbt:
        even_newer_entity_nbt[entity] = {}
        
        for key in new_entity_nbt[entity]:
            even_newer_entity_nbt[entity][key] = {}
            
            if type(new_entity_nbt[entity][key]) is dict:
                for key2 in new_entity_nbt[entity][key]:
                    
                    if key2 not in ["align", "tip", "label", "hide", "playerLookup", "doDropChance"]:
                        even_newer_entity_nbt[entity][key][key2] = new_entity_nbt[entity][key][key2]
            else:
                even_newer_entity_nbt[entity][key] = new_entity_nbt[entity][key]
                
    with open(f'{path}/data/entity_nbt.json', 'w') as f:
        f.write(json.dumps(even_newer_entity_nbt, indent=4))

def get_entity_nbt_json():
    entities = get_entity_list()
    get_entity_data(entities)
    reformat_entity_nbt()

# Utilities

def download_mcstacker_js_file():
    driver = get_mcstacker_driver()
    
    driver.get('https://mcstacker.net/mcstacker-1.19.min.js')
    
    js_content = driver.page_source

    # Removing any HTML tags that might be surrounding the JS content
    js_content = re.sub(r'<[^>]*>', '', js_content)
    
    # Unescape HTML entities
    js_content = html.unescape(js_content)
    
    js_content = jsbeautifier.beautify(js_content)
    
    with open(f"{path}/mcstacker.js", 'w') as file:
        file.write(js_content)

    clean_driver(driver)
    
def check_entity_subkeys():
    with open(f'{path}/data/entity_nbt.json') as f:
        entity_nbt = json.load(f)
        
    for entity in entity_nbt:
        for key in entity_nbt[entity]:
            if type(entity_nbt[entity][key]) is dict:
                for key2 in entity_nbt[entity][key]:
                    if key2 not in ["type", "format", "values", "choice"] and key2 not in ['fwClass']:
                        print(entity, key, key2, entity_nbt[entity][key][key2])

def get_mcstacker_content():

    with open(f"{path}/mcstacker.js", 'r') as file:
        content = file.read()
        
    return content

def extract_mcstacker_functions():
    
    content = get_mcstacker_content()

    # Matches top-level function declarations and expressions
    pattern = re.compile(r'^(?:function\s+([\w$]+)|([\w$]+)\s*=\s*function)\s*\(', re.MULTILINE)

    functions = []

    for match in pattern.finditer(content):
        function_name = match.group(1) or match.group(2)
        functions.append(function_name)

    print('\n'.join(functions))
    
    return functions

def extract_mcstacker_classes():
    
    content = get_mcstacker_content()

    # Matches class declarations
    pattern = re.compile(r'^\s*class\s+([\w$]+)', re.MULTILINE)

    classes = []

    for match in pattern.finditer(content):
        class_name = match.group(1)
        classes.append(class_name)

    print('\n'.join(classes))
    
    return classes

def get_mcstacker_func_and_classes():
    download_mcstacker_js_file()
    functions = extract_mcstacker_functions()
    classes = extract_mcstacker_classes()
    os.remove(f"{path}/mcstacker.js")
    
    return functions, classes