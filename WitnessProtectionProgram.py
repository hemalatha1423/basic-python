import json

class Witness:
    def __init__(self, witness_id, name, new_identity, location, protection_level):
        self.witness_id = witness_id
        self.name = name
        self.new_identity = new_identity
        self.location = location
        self.protection_level = protection_level

    def __str__(self):
        return f"ID: {self.witness_id}, Name: {self.name}, New Identity: {self.new_identity}, Location: {self.location}, Protection Level: {self.protection_level}"


class WitnessProtectionProgram:
    def __init__(self, filename="witnesses.json"):
        self.filename = filename
        self.load_witnesses()

    def load_witnesses(self):
        try:
            with open(self.filename, "r") as file:
                self.witnesses = json.load(file)
        except FileNotFoundError:
            print("No witness data found. Starting with an empty list.")
            self.witnesses = []

    def save_witnesses(self):
        with open(self.filename, "w") as file:
            json.dump(self.witnesses, file, indent=4)

    def add_witness(self):
        witness_id = input("Enter witness ID: ")
        name = input("Enter name: ")
        new_identity = input("Enter new identity: ")
        location = input("Enter location: ")
        protection_level = input("Enter protection level (High or Medium or Low): ")
        witness = Witness(witness_id, name, new_identity, location, protection_level)
        self.witnesses.append(witness.__dict__)
        self.save_witnesses()
        print("Witness added successfully.")

    def update_witness(self):
        witness_id = input("Enter witness ID to update: ")
        for witness in self.witnesses:
            if witness['witness_id'] == witness_id:
                name = input(f"Enter new name for witness {witness_id}: ") or witness['name']
                new_identity = input(f"Enter new identity for witness {witness_id}: ") or witness['new_identity']
                location = input(f"Enter new location for witness {witness_id}: ") or witness['location']
                protection_level = input(f"Enter new protection level for witness {witness_id}: ") or witness['protection_level']
                witness.update({'name': name, 'new_identity': new_identity, 'location': location, 'protection_level': protection_level})
                self.save_witnesses()
                print(f"Witness {witness_id} updated successfully.")
                return
        print("Witness not found.")

    def delete_witness(self):
        witness_id = input("Enter witness ID to delete: ")
        for idx, witness in enumerate(self.witnesses):
            if witness['witness_id'] == witness_id:
                del self.witnesses[idx]
                self.save_witnesses()
                print(f"Witness {witness_id} deleted successfully.")
                return
        print("Witness not found.")

    def print_witness_details(self):
        witness_id = input("Enter witness ID to print details: ")
        for witness in self.witnesses:
            if witness['witness_id'] == witness_id:
                print(f"ID: {witness['witness_id']}, Name: {witness['name']}, New Identity: {witness['new_identity']}, Location: {witness['location']}, Protection Level: {witness['protection_level']}")
                return
        print("Witness not found.")

    def manage_protected_witnesses(self):
        high_or_medium_witnesses = [witness for witness in self.witnesses if witness['protection_level'] in ["High", "Medium"]]
        if high_or_medium_witnesses:
            print("List of Protected Witnesses:")
            for witness in high_or_medium_witnesses:
                print(f"ID: {witness['witness_id']}, Name: {witness['name']}, New Identity: {witness['new_identity']}, Location: {witness['location']}, Protection Level: {witness['protection_level']}")
        else:
            print("No witnesses with High or Medium protection level.")

    def ensure_witness_safety(self):
        witness_id = input("Enter witness ID to check safety: ")
        for witness in self.witnesses:
            if witness['witness_id'] == witness_id:
                safe_locations = ["Home", "Safehouse", "Secure Facility"]
                if witness['location'] in safe_locations:
                    print(f"Witness {witness_id} is currently at a safe location.")
                else:
                    print(f"Witness {witness_id} may be at risk as they are not at a safe location.")
                return
        print("Witness not found.")

    def run(self):
        while True:
            print("\nWitness Protection Program Menu:")
            print("       1. Add Witness              ")
            print("       2. Update Witness           ")
            print("       3. Delete Witness            ")
            print("       4. Print Witness Details     ")
            print("       5. Manage Protected Witnesses")
            print("       6. Ensure Witness Safety     ")
            print("       7. Exit Program              ")
            option = input("Enter your choice: ")
            if option == '1':
                self.add_witness()
            elif option == '2':
                self.update_witness()
            elif option == '3':
                self.delete_witness()
            elif option == '4':
                self.print_witness_details()
            elif option == '5':
                self.manage_protected_witnesses()
            elif option == '6':
                self.ensure_witness_safety()
            elif option == '7':
                print("Exiting program.")
                break
            else:
                print("Invalid option. Please try again.")

# Example usage:
wpp = WitnessProtectionProgram()
wpp.run()
