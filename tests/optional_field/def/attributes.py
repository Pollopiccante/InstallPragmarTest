from tests.optional_field.gen.classes import Def
from tests.optional_field.gen.nodes import SomeTreeNode


@Def.SomeTreeNode
def test_attribute(node: SomeTreeNode) -> str:
    out = f"{node.myname}"
    for child in node.get_children():
        if child:
            out += child.attributes_test_attribute()
    return out
