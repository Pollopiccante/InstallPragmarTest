from PRAGMAR.decorators import def_run
from PRAGMAR.tree import AllParentNode
from tests.most_specific_inheritor.gen.nodes import A, B, C, D


@def_run
def run(ap: AllParentNode):

    test_d = D(8)
    tree = A(B(C(test_d), C(D(6))), B(C(D(5)), C(D(2))))

    ap.add_ast(tree)

    print(test_d.attributes_test())

    assert test_d.attributes_test() == "Inherited from A"
