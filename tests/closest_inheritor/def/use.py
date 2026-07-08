from PRAGMAR.decorators import def_run
from tests.closest_inheritor.gen.nodes import SomeLeafNode, SomeInnerNode, AllParent


# create AST
@def_run
def run(ap):
    ap: AllParent = AllParent.wrap(ap)

    test_leaf = SomeLeafNode()
    tree = (
        ap.create_SomeInnerNode(
            ap.create_SomeInnerNode(
                SomeLeafNode(),
                test_leaf,
                "inner_context"),
            ap.create_SomeLeafNode(),
            "outer_context"
        )
    )

    ap.prag_add_ast(tree)

    level_one_context = test_leaf.attributes_level_one_inherit()
    print(level_one_context)
    level_two_context = test_leaf.attributes_level_two_inherit()
    print(level_two_context)

    assert level_one_context == "inner_context"
    assert level_two_context == "outer_context"
