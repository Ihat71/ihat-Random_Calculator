import xml.sax

class Handling(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == 'customer':
            print("----Customer----", f"ID: {attrs['id']}", sep='\n')
            self.current_customer = "customer"
        if self.current == 'address':
            print("----Address----")
            self.current_address = "address"
    def characters(self, content):
        if self.current == "name":
            self.name_1 = content
        elif self.current == "street":
            self.street = content
        elif self.current == "city":
            self.city = content
        elif self.current == "state":
            self.state = content 
        elif self.current == "zip":
            self.zip = content
    def endElement(self, name):
        if self.current == "name":
            print(f"Name: {self.name_1}")
        elif self.current == "street":
            print(f"Street: {self.street}")
        elif self.current == "city":
            print(f"City: {self.city}")
        elif self.current == "state":
            print(f"State: {self.state}")
        elif self.current == "zip":
            print(f"Zip: {self.zip}")
        elif name == "address":
            print(f"--End of Address--")
            self.current_address = ""

        self.current = ''
handling = Handling()
parser = xml.sax.make_parser()
parser.setContentHandler(handling)
parser.parse(r'C:\Users\MIQDAD\Python\Learn\ne_sam.xml')
    