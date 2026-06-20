from tests.optional_field.gen.classes import Def
from tests.optional_field.gen.nodes import SomeTreeNode


@Def.SomeTreeNode
def test_attribute(node: SomeTreeNode) -> str:
    out = f"{node.attrib["myname"]}"
    for child in node.node_children:
        if child:
            out += child.attribute("test_attribute")()
    return out
