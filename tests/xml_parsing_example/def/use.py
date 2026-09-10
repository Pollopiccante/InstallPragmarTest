from PRAGMAR.decorators import def_run
from tests.xml_parsing_example.gen.nodes import AllParentNode, AllParent, SomeTreeNode


@def_run
def run(ap: AllParentNode):#
    xml_prefix = "./tests/xml_parsing_example/"
    schema = "note.xsd"
    xml_file = "note.xml"

    ap: AllParent = AllParent.wrap(ap)

    ap.parser_generate_xml_schema(xml_prefix + schema, "my_namespace", True)
    ap.parser_add_xml(xml_prefix + xml_file)

    ast: SomeTreeNode = ap.asts[0]

    ast.print_ast_print_tree(True, True)
    res = ast.attributes_test_attribute()


    print(res)
    assert res == "ABCD"
