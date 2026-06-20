from PRAGMAR.decorators import def_run
from PRAGMAR.new_tree import AllParentNode

from tests.optional_field.gen.nodes import SomeTreeNode


@def_run
def run(ap: AllParentNode):

    tree = SomeTreeNode.save_create(
        "A",
        SomeTreeNode.save_create(
            "B",
            None,
            SomeTreeNode.save_create("C", None, None)),
        SomeTreeNode.save_create("D", None, None)
    )
    ap.add_ast(tree)
    print(tree.attributes_test_attribute())

    assert tree.attributes_test_attribute() == "ABCD"
