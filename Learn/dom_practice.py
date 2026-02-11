import xml.dom.minidom

tree = xml.dom.minidom.parse(r'C:\Users\MIQDAD\Python\Learn\wor.xml')
group = tree.documentElement
persons = group.getElementsByTagName('person')
for person in persons:
    print('--person--')
    if person.hasAttribute('id'):
        print(f"{person.getAttribute('id')}")
    print(f"name: {person.getElementsByTagName('name')[0].childNodes[0].data}")
    print(f"age: {person.getElementsByTagName('age')[0].childNodes[0].data}")
    print(f"email: {person.getElementsByTagName('email')[0].childNodes[0].data}")
books = group.getElementsByTagName('book')
for book in books:
    print('---Book---')
    print(f"Title: {book.getElementsByTagName('title')[0].childNodes[0].data}")
    print(f"Author: {book.getElementsByTagName('author')[0].childNodes[0].data}")

#books[1].getElementsByTagName('title')[0].childNodes[0].nodeValue = "new name" #the node value gives us the value of the name which we will change
#you can also do books[0].setAttribute('id', '100) if you want to change an attribute
#tree.writexml(open(r'C:\Users\MIQDAD\Python\Learn\new_wor.xml', 'w')) #we wrote this change into a new xml file, but you can also write it into the original
new_person = tree.createElement("person")
new_person.setAttribute('id', '6')

name = tree.createElement('name')
name.appendChild(tree.createTextNode('Green')) #independant element with a child element (text) of "Green"
new_person.appendChild(name) #appends the element name as a child element to 'new_person'
group.appendChild(new_person) #important, of course
#note that once this is created, the new node will not be indented.
tree.writexml(open(r'C:\Users\MIQDAD\Python\Learn\new_wor.xml', 'w'))