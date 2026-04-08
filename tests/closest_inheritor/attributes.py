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
        def level_one_inherit(node: SomeInnerNode) -> str:
            return node.context_value

        @my_aspect.SomeInnerNode.SomeInnerNode.SomeLeafNode
        def level_two_inherit(node: SomeInnerNode) -> str:
            return node.context_value


if __name__ == "__main__":
    gen_attributes()