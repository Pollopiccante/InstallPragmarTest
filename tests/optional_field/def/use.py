from PRAGMAR.decorators import def_run
from PRAGMAR.new_tree import AllParentNode

from tests.optional_field.gen.nodes import SomeTreeNode, AllParent


@def_run
def run(ap: AllParentNode):
    ap: AllParent = AllParent.wrap(ap)

    tree = ap.create_SomeTreeNode(
        "A",
        ap.create_SomeTreeNode(
            "B",
            None,
            ap.create_SomeTreeNode("C",None, None)),
        ap.create_SomeTreeNode("D", None, None)
    )


    ap.prag_add_ast(tree)
    print(tree.attributes_test_attribute())

    assert tree.attributes_test_attribute() == "ABCD"
