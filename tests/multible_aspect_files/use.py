from PRAGMAR.core_aspects.pragmar import ap
from attributes import gen_attributes
from gen.classes import SomeInnerNode, SomeLeafNode


# create AST
def run():
    gen_attributes()

    tree = (
        SomeInnerNode(
            SomeInnerNode(
                SomeLeafNode(),
                SomeLeafNode(),
                "inner_context"),
            SomeLeafNode(),
            "outer_context"
        ))


    ap.add_ast(tree)

    print(tree.my_dark_aspect_run())
    print(tree.my_light_aspect_run())

if __name__ == '__main__':
    run()