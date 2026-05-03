from PRAGMAR.decorators import def_grammar
from PRAGMAR.tree import GrammarBuilder

# define grammar
@def_grammar
def gen_grammar(grammar: GrammarBuilder):
    (grammar.Head("SomeNode"))
    (grammar.Head("SomeLeafNode", head_super_type="SomeNode"))
    (grammar.Head("SomeInnerNode", head_super_type="SomeNode")
     .Field(field_name="child1", field_type="SomeNode")
     .Field(field_name="child2", field_type="SomeNode"))
