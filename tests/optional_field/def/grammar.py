from PRAGMAR.decorators import def_grammar
from PRAGMAR.tree import GrammarBuilder


@def_grammar
def my_grammar(grammar: GrammarBuilder):
    (grammar.Head("SomeTreeNode")
     .Field(field_type=str, field_name="myname")
     .Field(field_type="SomeTreeNode", field_name="child1", optional=True)
     .Field(field_type="SomeTreeNode", field_name="child2", optional=True))