'''
Tools for easier usage of components
'''

def flatten(component):
    if hasattr(component, "to_str"):
        return component.to_str()
    elif isinstance(component, str):
        return component
    else:
        return ''

def execute_check(response):
    if response == 'Test passed':
        return True
    elif response == 'Test failed':
        return False
    else:
        return response