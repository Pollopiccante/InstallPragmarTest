from PRAGMAR.core_aspects.pragmar import ap
from tests.inherit_name_over_type.attributes import gen_attributes
from gen.classes import SomeInnerNode, SomeLeafNode


# create AST
def run():
    gen_attributes()

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

    child1_result = test_leaf1.my_aspect_test_inherit()
    print(child1_result)
    child1_resul2 = test_leaf2.my_aspect_test_inherit()
    print(child1_resul2)

    assert child1_result == "child1_context"
    assert child1_resul2 == "child_type_context"

if __name__ == '__main__':
    run()