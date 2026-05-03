"""
This test-case mirrors the inherit_name_over_type case.
But is implemented without generated code.
Grammar and Attribute definitions are dynamically added.
This is the same Behavior that happens under the hood when generated code is used.
"""

from PRAGMAR.core_aspects.pragmar import load_ap
from PRAGMAR.tree import TreeNode, InnerNode

def run():
    ap = load_ap()

    # grammar definition
    grammar = ap.create_grammar()
    (grammar.Head("SomeNode"))
    (grammar.Head("SomeLeafNode", head_super_type="SomeNode"))
    (grammar.Head("SomeInnerNode", head_super_type="SomeNode")
     .Field(field_name="child1", field_type="SomeNode")
     .Field(field_name="child2", field_type="SomeNode"))

    # aspect definition
    my_aspect = ap.create_aspect("my_aspect")
    @my_aspect.Type("SomeInnerNode").Type("SomeLeafNode").Value()
    def test_inherit(node) -> str:
        return "child_type_context"

    @my_aspect.Type("SomeInnerNode").Name("child1").Value()
    def test_inherit(node) -> str:
        return "child1_context"

    # use
    def create_some_leaf():
        return TreeNode("SomeLeafNode")
    def create_some_inner(child1, child2):
        node = InnerNode("SomeInnerNode")
        node.add_child("child1", child1)
        node.add_child("child2", child2)
        return node

    test_leaf1 = create_some_leaf()
    test_leaf2 = create_some_leaf()
    tree = (
        create_some_inner(
            create_some_inner(
                test_leaf1,
                test_leaf2,
            ),
            create_some_leaf(),
        )
    )

    ap.add_ast(tree)

    # dynamic calling of attributes:
    # attribute("some_attr_name") returns the attribute-function
    # the function can then be called with its arguments (zero in this case)
    child1_result = test_leaf1.attribute("test_inherit")()
    print(child1_result)
    child2_result = test_leaf2.attribute("test_inherit")()
    print(child2_result)

    assert child1_result == "child1_context"
    assert child2_result == "child_type_context"

if __name__ == "__main__":
    run()