#!/usr/local/bin/python3
#!/usr/local/bin/python3
#
# Paul Evans (10evans@cua.edu)
# 6 November 2016
#
import re
import string
import xml.etree.ElementTree as ET
import Samples
def main():
    builder = ET.TreeBuilder()
    builder.start('django-objects', { 'version': '1.0' } )
    for i in range(len(Samples.listofdicts)):
        builder.start('object', { 'model': 'ingobert.sample' } )
        builder.start('field', { 'name': 'project', 'type': 'CharField' } )
        builder.data(Samples.listofdicts[i]['project'])
        builder.end('field')
        builder.start('field', { 'name': 'source', 'type': 'CharField' } )
        builder.data(Samples.listofdicts[i]['source'])
        builder.end('field')
        builder.start('field', { 'name': 'label', 'type': 'CharField' } )
        builder.data(Samples.listofdicts[i]['label'])
        builder.end('field')
        builder.start('field', { 'name': 'text', 'type': 'TextField' } )
        text = Samples.listofdicts[i]['text']
        text = re.sub('['+string.punctuation+']', '', text)
        text = text.lower()
        #
        # text = text.replace('cia', 'tia')
        # text = text.replace('cio', 'tio')
        # text = text.replace('ae', 'e')
        # text = text.replace('V', 'U')
        # text = text.replace('v', 'u')
        #
        builder.data(text)
        builder.end('field')
        builder.end('object')
    builder.end('django-objects')
    root = builder.close()
    ET.dump(root)
if __name__ == '__main__':
    main()

