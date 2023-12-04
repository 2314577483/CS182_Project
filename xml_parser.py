from lxml import etree
import sys

def check_xml_validity(xml_file):
    try:
        etree.parse(xml_file)
        print(f"XML file {xml_file} is syntactically valid.")
        return True
    except etree.XMLSyntaxError as e:
        print(f"Error: Unable to parse XML file {xml_file}\n{e}")
        return False

def main():
    # if a filename is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <xml_file>")
        sys.exit(1)

    xml_file = sys.argv[1]

    if check_xml_validity(xml_file):

if __name__ == "__main__":
    main()
