import sys
from xml.etree import ElementTree


def convert(tree):
    root = tree.getroot()
    new_root = convert_node(root)
    new_tree = ElementTree.ElementTree(new_root)
    return new_tree

def convert_node(node):
    result = None
    if node.tag == 'a':
        result = convert_a(node)
    elif node.tag == 'dfn':
        result = convert_dfn(node)
    elif node.tag == 'math':
        result = convert_math(node)
    elif node.tag == 'p':
        result = convert_p(node)
    elif node.tag == 'page':
        result = convert_page(node)
    elif node.tag == 'section':
        result = convert_section(node, 2)
    else:
        raise NotImplementedError('No such tag: {}'.format(node.tag))
    return result

def add_children(node, new_node):
    for child in node:
        new_child = convert_node(child)
        new_node.append(new_child)

def copy_node(node):
    result = ElementTree.Element(node.tag)
    result.attrib = node.attrib
    result.text = node.text
    result.tail = node.tail
    return result

def convert_a(node):
    return copy_node(node)    

def convert_dfn(node):
    return copy_node(node)

def convert_math(node):
    result = ElementTree.Element('span')
    result.text = '${}$'.format(node.text)
    result.tail = node.tail
    return result

def convert_p(node):
    result = copy_node(node)
    add_children(node, result)
    return result

def convert_page(node):
    result = ElementTree.Element('article')
    result.attrib = {'id': 'content'}
    heading = ElementTree.Element('h1')
    heading.text = node.attrib['title']
    result.append(heading)
    add_children(node, result)
    return result

def convert_section(node, level):
    result = ElementTree.Element('section')
    heading = ElementTree.Element('h{}'.format(level))
    heading.text = node.attrib['title']
    result.append(heading)
    result.text = node.text
    result.tail = node.tail
    add_children(node, result)
    return result
