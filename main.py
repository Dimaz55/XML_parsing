import xml.etree.ElementTree as ET
from collections import Counter
from pprint import pprint


def main():
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    xml_item = root.findall('channel/item/description')
    words = []
    for item in xml_item:
        word = [word for word in item.text.split() if len(word) > 6]
        words.extend(word)
    top = Counter(words)
    pprint(top.most_common(10))


if __name__ == '__main__':
    main()
