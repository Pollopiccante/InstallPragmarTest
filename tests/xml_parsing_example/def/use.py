from PRAGMAR.decorators import def_run
from tests.xml_parsing_example.gen.nodes import AllParentNode, AllParent

@def_run
def run(ap: AllParentNode):#
    xml_prefix = "./tests/xml_parsing_example/"
    schema = "note.xsd"
    xml_file = "note.xml"

    ap: AllParent = AllParent.wrap(ap)

    ap.parser_generate_xml_schema(xml_prefix + schema, "my_namespace", True)
    tree = ap.parser_add_xml(xml_prefix + xml_file)

    res = tree.attribute("test_attribute")()
    print(res)
    assert res == "ABCD"
