from PRAGMAR.decorators import def_run
from PRAGMAR.new_tree import AllParentNode

from tests.multible_aspect_files.gen.nodes import SomeInnerNode, SomeLeafNode, AllParent


# create AST
@def_run
def run(ap: AllParentNode):
    ap: AllParent = AllParent.wrap(ap)

    tree = (
        ap.create_SomeInnerNode(
            ap.create_SomeInnerNode(
                ap.create_SomeLeafNode(),
                ap.create_SomeLeafNode(),
                "inner_context"),
            ap.create_SomeLeafNode(),
            "outer_context"
        ))


    ap.prag_add_ast(tree)

    print(tree.dark_run_dark())
    print(tree.light_run_light())
    print(tree.cyan_run_cyan())

if __name__ == '__main__':
    run()