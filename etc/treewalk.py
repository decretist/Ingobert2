#! /usr/local/bin/python3
#
# Paul Evans (10evans@cua.edu)
# 16 October 2016
#
import xml.etree.ElementTree as ET
def main():
    tree = ET.parse('./upload.xml')
    root = tree.getroot()
    for capitulum in root:
        # ET.dump(capitulum)
        number = capitulum[0].text
        source = capitulum[1].text
        text = capitulum[3].text
        print('c. ' + number)
        print(source)
        print(text)
if __name__ == '__main__':
    main()
