from PRAGMAR.decorators import def_run
from tests.closest_inheritor.gen.nodes import SomeLeafNode, SomeInnerNode

# create AST
@def_run
def run(ap):
    test_leaf = SomeLeafNode()
    tree = (
        SomeInnerNode(
            SomeInnerNode(
                SomeLeafNode(),
                test_leaf,
                "inner_context"),
            SomeLeafNode(),
            "outer_context"
        )
    )

    ap.add_ast(tree)

    level_one_context = test_leaf.attributes_level_one_inherit()
    print(level_one_context)
    level_two_context = test_leaf.attributes_level_two_inherit()
    print(level_two_context)

    assert level_one_context == "inner_context"
    assert level_two_context == "outer_context"
