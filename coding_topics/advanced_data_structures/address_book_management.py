class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name: str, phone_number: str) -> bool:
        if name in self.contacts:
            return False
        self.contacts[name] = phone_number
        return True

    def get_contact(self, name: str) -> str | None:
        return self.contacts.get(name)

    def delete_contact(self, name: str) -> bool:
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False


if __name__ == "__main__":
    address_book = AddressBook()
    address_book.add_contact("Alice", "123-456-7890")

    print(address_book.delete_contact("Alice"))
    print(address_book.delete_contact("Bob"))
    print(address_book.contacts)
