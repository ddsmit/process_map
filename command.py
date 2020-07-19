from data import crud as crud
from data import search as search

commands = {
        'addsibling':{
            'func':crud.add_sibling,
            'label':'Add sibling to current node.',
            },
        'addchild':{
            'func':crud.add_child,
            'label':'Add child to current node.',
            },
        'deletenode':{
            'func':crud.delete_node,
            'label':'Delete current node(s)',
            },
        'addedge':{
            'func':crud.add_edge_last_current,
            'label':'Add edge from first and 2nd node',
            },
        'movetonextsibling':{
            'func':search.move_to_next_sibling,
            'label':'Move to the next sibling',
            },
        'movetoprevioussibling':{
            'func':search.move_to_previous_sibling,
            'label':'Move to the previous sibling',
            },
        'movetoparentnode':{
            'func':search.move_to_parent,
            'label':'Move to the parent node',
            },
        'movetofirstchild':{
            'func':search.move_to_first_child,
            'label':'Move to first child node',
            },
    }

def build_options():
    return [
        {'label':data['label'],'value':value}
        for value, data in commands.items()
    ]

def no_input():
    return ''

def get_functions(input_string):
    return None
    if input_string:
        return [commands[char] for char in input_string if char in commands]
    else:
        return [no_input]