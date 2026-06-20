from tests.xml_parsing_example.gen.classes import Def
from tests.xml_parsing_example.gen.nodes import SomeTreeNode


@Def.SomeTreeNode
def test_attribute(node: SomeTreeNode) -> str:
    out = f"{node.data["myname"]}"
    for child in node.node_children:
        if child is not None:
            out += child.attribute("test_attribute")()
    return out
