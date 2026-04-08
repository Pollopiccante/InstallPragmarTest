from PRAGMAR.core_aspects.pragmar import ap
from gen.classes import SomeInnerNode
from gen.classes import Def

from grammar import gen_grammar


# define grammar
def gen_attributes():
    gen_grammar()

    # define aspects
    with ap.define_attributes(Def):
        my_aspect = Def.create_aspect("my_aspect")

        @my_aspect.SomeInnerNode.SomeLeafNode
        def test_inherit(node: SomeInnerNode) -> str:
            return "child_type_context"

        @my_aspect.SomeInnerNode.child1
        def test_inherit(node: SomeInnerNode) -> str:
            return "child1_context"


if __name__ == "__main__":
    gen_attributes()