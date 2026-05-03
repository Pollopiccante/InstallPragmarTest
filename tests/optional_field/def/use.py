from PRAGMAR.decorators import def_run
from PRAGMAR.tree import AllParentNode

from tests.optional_field.gen.nodes import SomeTreeNode


@def_run
def run(ap: AllParentNode):

    tree = SomeTreeNode(
        "A",
        SomeTreeNode(
            "B",
            None,
            SomeTreeNode("C", None, None)),
        SomeTreeNode("D", None, None)
    )
    ap.add_ast(tree)
    print(tree.attributes_test_attribute())

    assert tree.attributes_test_attribute() == "ABCD"
