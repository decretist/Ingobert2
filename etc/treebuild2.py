#!/usr/local/bin/python3 #
# Paul Evans (10evans@cua.edu)
# 26 November 2016
#
import re
import string
import xml.etree.ElementTree as ET
def main():
    tree = ET.parse('./upload.xml')
    root = tree.getroot()
    builder = ET.TreeBuilder()
    builder.start('django-objects', { 'version': '1.0' } )
    for capitulum in root:
        project = 'Capitulare Carisiacense'
        source = capitulum[1].text
        label = 'cap. ' + capitulum[0].text
        text = capitulum[3].text
        if (text != None):
            text = re.sub('\s+', ' ', text)
            text = re.sub('^\s+', '', text)
            text = re.sub('\s+$', '', text)
            builder.start('object', { 'model': 'ingobert.sample' } )
            builder.start('field', { 'name': 'project', 'type': 'CharField' } )
            builder.data(project)
            builder.end('field')
            builder.start('field', { 'name': 'source', 'type': 'CharField' } )
            builder.data(source)
            builder.end('field')
            builder.start('field', { 'name': 'label', 'type': 'CharField' } )
            builder.data(label)
            builder.end('field')
            builder.start('field', { 'name': 'text', 'type': 'TextField' } )
            builder.data(text)
            builder.end('field')
            builder.end('object')
    builder.end('django-objects')
    root = builder.close()
    ET.dump(root)

if __name__ == '__main__':
    main()

