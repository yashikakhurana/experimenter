"""
This type stub file was generated by pyright.
"""

from future.utils import with_metaclass
from parsimonious import NodeVisitor

def operator_pattern(operators):  # -> str:
    """Generate a grammar rule to match a dict of operators."""
    ...

def jexl_grammar(jexl_config): ...

class Parser(NodeVisitor):
    def __init__(self, jexl_config) -> None: ...
    def visit_expression(self, node, children): ...
    def visit_subexpression(self, node, children): ...
    def visit_binary_expression(self, node, children): ...
    def visit_conditional_expression(self, node, children): ...
    def visit_conditional_test(self, node, children): ...
    def visit_binary_operator(self, node, children): ...
    def visit_binary_operand(self, node, children): ...
    def visit_unary_expression(self, node, children): ...
    def visit_unary_operator(self, node, children): ...
    def visit_unary_operand(self, node, children): ...
    def visit_object_literal(self, node, children): ...
    def visit_object_key_value_list(self, node, children): ...
    def visit_object_key_value(self, node, children): ...
    def visit_array_literal(self, node, children): ...
    def visit_value_list(self, node, children): ...
    def visit_complex_value(self, node, children): ...
    def visit_attribute(self, node, children): ...
    def visit_transform(self, node, children): ...
    def visit_transform_arguments(self, node, children): ...
    def visit_filter_expression(self, node, children): ...
    def visit_identifier(self, node, children): ...
    def visit_relative_identifier(self, node, children): ...
    def visit_value(self, node, children): ...
    def visit_boolean(self, node, children): ...
    def visit_numeric(self, node, children): ...
    def visit_string(self, node, children): ...
    def generic_visit(self, node, visited_children): ...

class NodeMeta(type):
    """
    Metaclass for making AST nodes. Handles adding the Node's custom
    fields to __slots__ and ensures every Node has a parent field.
    """

    def __new__(meta, classname, bases, classdict): ...

class Node(with_metaclass(NodeMeta, object)):
    """
    Base class for AST Nodes.

    Nodes are like mutable namedtuples. Each node type should declare a
    fields attribute on the class that lists the desired attributes for
    the class.
    """

    fields = ...
    def __init__(self, *args, **kwargs) -> None:
        """
        Accepts values for this node's fields as both positional (in the
        order defined in self.fields) and keyword arguments.
        """
        ...
    def __repr__(self): ...
    def __eq__(self, other) -> bool: ...
    @property
    def children(self): ...
    def root(self): ...
    def contains_relative(self): ...

class BinaryExpression(Node):
    fields = ...
    @property
    def children(self): ...

class UnaryExpression(Node):
    fields = ...
    @property
    def children(self): ...

class Literal(Node):
    fields = ...

class Identifier(Node):
    fields = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def children(self): ...

class ObjectLiteral(Node):
    fields = ...

class ArrayLiteral(Node):
    fields = ...

class Transform(Node):
    fields = ...
    @property
    def children(self): ...

class FilterExpression(Node):
    fields = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def children(self): ...
    def contains_relative(self): ...

class ConditionalExpression(Node):
    fields = ...
    @property
    def children(self): ...
