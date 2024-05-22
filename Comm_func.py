'''
This is a common functions file.
All the regular used functions are added here.
'''


import hou
obj_context = hou.node('/obj')


def create_context(node_name=None, node_path=None):
    '''
    create parent node_context
    node_name :: string : "body_Geo"
    :return: object:: "<hou.ObjNode of type geo at /obj/body_GEO>"
    '''
    if node_name:
        create_node_path = '/obj' + "/" + node_name
        node_context = hou.node(create_node_path)
    else:
        node_context = hou.node(node_path)
    return node_context


def get_parent_nodes(work_area=None):
    '''
    get all the childs of the parent context
    work_area:: object :  obj_context
    :return: list: [{]'head_GEO', 'body_GEO', 'hair_GEO']
    '''
    parent_list = []
    children_nodes = work_area.children()
    for node in children_nodes:
        parent_list.append(node.name())
    return parent_list


def get_child_nodes(parent=None):
    '''
    get all the childs of the parent context
    :return: list : child list ("<hou.SopNode of type alembic at /obj/head_GEO/alembic1>, <hou.SopNode of type grid a
t /obj/head_GEO/grid1>, "
    '''
    child_nodes = parent.children()
    return child_nodes


def rename_cmd(parent_node=None, child_node=None):
    '''
    rename node command
    :return: None
    '''
    parent_node_name = parent_node.name()
    if "_" in parent_node_name:
        parent_suffix = parent_node_name.split("_")[0]
        # print(parent_suffix)
    if parent_suffix:
        new_name = parent_suffix + "_" + child_node.name().upper()
    # set new name
    child_node.setName(new_name)
    return None


def create_parent_child_dict():
    '''
    create dict with parent and child lists
    :return: dict:  {'head_GEO': ['/obj/head_GEO/alembic1', '/obj/head_GEO/grid1', '/obj/head_GEO/sc
ulpt1'], 'body_GEO': ['/obj/body_GEO/alembic1']}
    '''
    parent_node_list = {}

    # get parent nodes in obj context
    parent_nodes = get_parent_nodes(work_area = obj_context)

    # create parent context
    # get all child nodes of parent ,add them to a list
    # create a dict of all parents and childlist in format: parent:child_nodes_list
    for each_parent in parent_nodes:
        # print(each_parent) # "body_GEO"
        parent_context = create_context(node_name=each_parent, node_path=None)
        child_nodes = get_child_nodes(parent=parent_context)

        child_list = []
        for each_node in child_nodes:
            child_list.append(each_node.path())
        parent_node_list[each_parent] = child_list

    # print(parent_node_list)
    return parent_node_list


def rename_all_child_nodes():
    '''
    This is main function of this file to rename all child nodes
    :return: None
    '''
    parent_child_list = create_parent_child_dict()

    # get all parent and child list dict
    # extract each_parent from dict and create parent houdini node
    # extract each child_name from dict and create child houdini node
    # run rename function
    for each_parent in parent_child_list.keys():
        # print(each_parent)
        parent_node = create_context(node_name=each_parent, node_path=None)
        child_lists = parent_child_list[each_parent]
        # print(child_lists)
        for each_child in child_lists:
            child_node = create_context(node_name=None, node_path=each_child)
            rename_cmd(parent_node=parent_node, child_node=child_node)
            print("Set new Name: ", child_node.name())
    return None





















