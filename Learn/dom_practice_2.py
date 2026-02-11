import xml.dom.minidom

tree = xml.dom.minidom.parse(r'C:\Users\MIQDAD\Python\Learn\ne_sam.xml')
group = tree.documentElement
character = group.getElementsByTagName('customer')[0]
nam = character.getElementsByTagName('name')[0]
addy = character.getElementsByTagName('address')
print(nam.firstChild.data)
for i in addy:
    for j in i.childNodes:
        if j.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
            print(j.firstChild.data)





