from PRAGMAR.core_aspects.pragmar import ap
from tests.closest_inheritor.attributes import gen_attributes
from gen.classes import SomeInnerNode, SomeLeafNode


# create AST
def run():
    gen_attributes()

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

    level_one_context = test_leaf.my_aspect_level_one_inherit()
    print(level_one_context)
    level_two_context = test_leaf.my_aspect_level_two_inherit()
    print(level_two_context)

    assert level_one_context == "inner_context"
    assert level_two_context == "outer_context"

if __name__ == '__main__':
    run()