from tests.closest_inheritor.gen.classes import Def
from tests.closest_inheritor.gen.nodes import SomeInnerNode

@Def.SomeInnerNode.SomeLeafNode
def level_one_inherit(node: SomeInnerNode) -> str:
    return node.context_value

@Def.SomeInnerNode.SomeInnerNode.SomeLeafNode
def level_two_inherit(node: SomeInnerNode) -> str:
    return node.context_value
