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
        
def trim_file_name(file_name):
    return file_name.split('/')[-1]

