from PRAGMAR.decorators import def_run
from PRAGMAR.tree import AllParentNode

from tests.inherit_name_over_type.gen.nodes import SomeInnerNode, SomeLeafNode


@def_run
def run(ap: AllParentNode):
    test_leaf1 = SomeLeafNode()
    test_leaf2 = SomeLeafNode()
    tree = (
        SomeInnerNode(
            SomeInnerNode(
                test_leaf1,
                test_leaf2,
            ),
            SomeLeafNode(),
        )
    )

    ap.add_ast(tree)

    child1_result = test_leaf1.attributes_test_inherit()
    print(child1_result)
    child2_result = test_leaf2.attributes_test_inherit()
    print(child2_result)

    assert child1_result == "child1_context"
    assert child2_result == "child_type_context"

if __name__ == '__main__':
    run()