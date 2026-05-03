from PRAGMAR.decorators import def_run
from PRAGMAR.tree import AllParentNode

from tests.multible_aspect_files.gen.nodes import SomeInnerNode, SomeLeafNode


# create AST
@def_run
def run(ap: AllParentNode):
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

    print(tree.dark_run_dark())
    print(tree.light_run_light())
    print(tree.cyan_run_cyan())

if __name__ == '__main__':
    run()