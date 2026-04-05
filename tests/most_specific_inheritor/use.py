from PRAGMAR.core_aspects.pragmar import ap
from tests.most_specific_inheritor.attributes import gen_attributes
from gen.classes import A, B, C, D


# create AST
def run():
    gen_attributes()


    test_d = D(8)
    tree = A(B(C(test_d), C(D(6))), B(C(D(5)), C(D(2))))

    ap.add_ast(tree)

    print(test_d.my_aspect_test())

    assert test_d.my_aspect_test() == "Inherited from A"


if __name__ == '__main__':
    run()