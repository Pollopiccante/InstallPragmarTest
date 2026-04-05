import os

from PRAGMAR.core_aspects.pragmar import ap

from PRAGMAR.tree import AllParentNode

# set core generation directory
AllParentNode.GEN_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "gen")

# define grammar
def gen_grammar():
    with ap.define_grammar():
        grammar_def = ap.create_grammar()
        (grammar_def.Head("SomeNode"))
        (grammar_def.Head("SomeLeafNode", head_super_type="SomeNode"))
        (grammar_def.Head("SomeInnerNode", head_super_type="SomeNode")
         .Field(field_name="child1", field_type="SomeNode")
         .Field(field_name="child2", field_type="SomeNode"))


if __name__ == "__main__":
    gen_grammar()