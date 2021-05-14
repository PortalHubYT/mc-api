'''
Tools for easier usage of components
'''

def flatten(component):
    if hasattr(component, "to_str"):
        return component.to_str()
    else:
        return ''