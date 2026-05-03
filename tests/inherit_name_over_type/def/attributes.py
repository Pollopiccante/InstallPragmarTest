from tests.inherit_name_over_type.gen.nodes import SomeInnerNode
from tests.inherit_name_over_type.gen.classes import Def


@Def.SomeInnerNode.SomeLeafNode
def test_inherit(node: SomeInnerNode) -> str:
    return "child_type_context"

@Def.SomeInnerNode.child1
def test_inherit(node: SomeInnerNode) -> str:
    return "child1_context"

