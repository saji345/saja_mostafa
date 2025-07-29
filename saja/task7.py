contacts=[]
def add_new_contact():
    name=input("name?")
    phone=input("phone?")
    email=input("email?")
    contact={"name":name,"phone":phone,"email":email}     
    contacts.append(contact)
    print("new contact saved",contact)
def view_contacts():
    l=input("do you want to view your contacts?(yes or no)")
    if l == "yes":
        print(contacts)
def search_for_contact():
    name=input("enter contact name")
    for contact in contacts:
        if name == contact["name"]:
            print(contact)
def delete_contact():
    delete=(input("enter a contact to delete"))
    for contact in contacts:
        if delete == contact["name"]:
         contacts.remove(contact)
         print("contact deleted")
def show_options():
    print("add new contact") 
    print("delete a contact")
    print("view contacts")
    print("search for contact")
    print("back")
while True:
    show_options()
    s=input("choose option")
    if s == "add new contact":
        add_new_contact()
    elif s == "delete a contact":
        delete_contact()
    elif s == "view contacts":
        view_contacts()
    elif s == "search for contact":
        search_for_contact()
    elif s== "back":
        break
    

