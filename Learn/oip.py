import xml.sax

class RootHandler(xml.sax.ContentHandler):
    def startElement(self, name, attr):
        self.current = name #this tells us which node we are currently working with
        if self.current == "person":
            print("-----Person-----")
        if self.current == "book":
            print('-----Book-----')
    def characters(self, content): #this method deals with the info within the tags
        if self.current == "name":
            self.name = content #if I am dealing with a tag that is a name, I want to make a new attribute in my class and set it to the content
        elif self.current == "age":
            self.age = content
        elif self.current == "email":
            self.email = content
        elif self.current == "title":
            self.title = content
        elif self.current == "author":
            self.author = content
        elif self.current == "year":
            self.year = content
    def endElement(self, name):
        if self.current == "name":
            print(f'name: {self.name}')
        elif self.current == "age":
            print(f'age: {self.age}')
        elif self.current == "email":
            print(f'email: {self.email}')
        elif self.current == "title":
            print(f'title: {self.title}')
        elif self.current == "author":
            print(f'author: {self.author}')
        elif self.current == "year":
            print(f'year: {self.year}')
        self.current = '' # need to do this, resets it

handler = RootHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse(r'C:\Users\MIQDAD\Python\Learn\wor.xml') #use raw string to circumvent error