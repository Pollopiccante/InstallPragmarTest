from PRAGMAR.tree import GrammarBuilder
from PRAGMAR.decorators import def_grammar

@def_grammar
def gen_grammar(grammar: GrammarBuilder):
    print("DEFINING Grammar")
    (grammar.Head("SomeNode"))
    (grammar.Head("SomeLeafNode", head_super_type="SomeNode"))
    (grammar.Head("SomeInnerNode", head_super_type="SomeNode")
     .Field(field_name="child1", field_type="SomeNode")
     .Field(field_name="child2", field_type="SomeNode")
     .Field(field_name="context_value", field_type=str))


if __name__ == "__main__":
    gen_grammar()