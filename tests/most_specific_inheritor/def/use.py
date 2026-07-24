from PRAGMAR.decorators import def_run
from PRAGMAR.new_tree import AllParentNode
from tests.most_specific_inheritor.gen.nodes import A, B, C, D, AllParent


@def_run
def run(ap: AllParentNode):
    ap: AllParent = AllParent.wrap(ap)

    test_d = ap.create_D(8)
    tree = ap.create_A(
        ap.create_B(
            ap.create_C(
                test_d
            ),
            ap.create_C(
                ap.create_D(6)
            )
        ),
        ap.create_B(
            ap.create_C(
                ap.create_D(5)
            ),
            ap.create_C(
                ap.create_D(2)
            )
        )
    )

    ap.prag_add_ast(tree)

    print(test_d.attributes_test())

    assert test_d.attributes_test() == "Inherited from A"
