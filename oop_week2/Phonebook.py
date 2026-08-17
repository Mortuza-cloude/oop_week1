


"""""
Project: Create a phone Book
Features
-Add contact
-view contact
-Search contact
-Update contact
-Delete contact
"""""



class Contact:
    def __init__(self, contact_id, name, phone, address= None):
        self.contact_id= contact_id
        self.name= name
        self.phone= phone
        self.address= address
    def __str__(self):
        return f"ID: {self.contact_id} | Name: {self.name} Phone: {self.phone} |Address: {self.address}"

class PhoneBook:
    def __init__(self):
        self.contacts =[]
        self.next_id =1
#Add Contact
    def add_contact(self, name, phone, address= None):
        contact = Contact(self.next_id, name, phone, address)
        self.contacts.append(contact)
        self.next_id+=1
        print("Contacts Added")
        print(contact)


#view Contacts

    def view_contacts(self):
        print("====All Contacts===")
        for contact in self.contacts:
            print(contact)

#Search Contacts
    def search_contact(self, contact_id):
        for contact in self.contacts:
            if contact.contact_id== contact_id:
                print("contact Found")
                print(contact)
                return
        print("No Contact Found")


#Update Contact

    def update_contact(self, contact_id, new_phone, new_address):
        for contact in self.contacts:
            if contact.contact_id== contact_id:
                contact.phone= new_phone
                contact.address = new_address
                print("contact Updated")
                print(contact)
                return
        print("No Contact Found")



#Delete Contact
    
    def delete_contact(self, contact_id):
        for contact in self.contacts:
            if contact.contact_id== contact_id:
                self.contacts.remove(contact)
                print("Contact Deleted")
                return
        print("No Contact Found")
        

        
        


kutni = PhoneBook()
kutni.add_contact("Mahi", "01394232")
kutni.add_contact("Niloy", "032322", "Osaka")
kutni.add_contact("troy", "284372", "kyoto")
kutni.add_contact("Joy", "2432423", "Kobe")

kutni.delete_contact(1)
kutni.view_contacts()