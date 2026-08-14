import csv

# Class representing a single room
class Room:
    def __init__(self, rid, rtype, price):
        self.rid = rid        # Room ID
        self.rtype = rtype    # Room type (1B, 2B, 3B, S)
        self.price = price    # Room price
        self.booked = False   # Booking status

    def __str__(self):
        status = "Booked" if self.booked else "Avail"
        return f"ID: {self.rid}, Type: {self.rtype}, Price: {self.price}, Status: {status}"


# Class representing the hotel system
class Hotel:
    def __init__(self):
        self.rms = []  # List of rooms

    # Add a new room
    def add_room(self, rid, rtype, price):
        # validate type
        if rtype not in ["1B", "2B", "3B", "S"]:
            print("Invalid room type. Use 1B, 2B, 3B, or S.")
            return
        # check duplicate ID
        for rm in self.rms:
            if rm.rid == rid:
                print("Room ID already exists.")
                return
        # add room
        self.rms.append(Room(rid, rtype, price))
        print("Room added.")

    # View all rooms
    def view_rooms(self):
        if not self.rms:
            print("No rooms.")
        else:
            print(f"{'ID':<10}{'Type':<10}{'Price':<10}{'Status':<10}")
            print("-" * 40)
            for rm in self.rms:
                status = "Booked" if rm.booked else "Avail"
                print(f"{rm.rid:<10}{rm.rtype:<10}{rm.price:<10}{status:<10}")

    # Search for rooms by type code (1B, 2B, 3B, S)
    def search_room(self, rtype):
        found = [rm for rm in self.rms if rm.rtype == rtype]
        if found:
            for rm in found:
                print(rm)
        else:
            print("No rooms of this type.")

    # Show available rooms of a type and allow booking
    def book_room(self, rtype):
        avail = [rm for rm in self.rms if rm.rtype == rtype and not rm.booked]
        if not avail:
            print("No available rooms of this type.")
            return
        print("Available rooms:")
        for rm in avail:
            print(rm)
        rid = input("Enter Room ID to book: ")
        for rm in avail:
            if rm.rid == rid:
                rm.booked = True
                print("Room booked.")
                return
        print("Invalid Room ID.")

    # Cancel a booking by ID
    def cancel_book(self, rid):
        for rm in self.rms:
            if rm.rid == rid and rm.booked:
                rm.booked = False
                print("Booking cancelled.")
                return
        print("Invalid cancel.")

    # Save hotel data to file
    def save_file(self, fname="DAY 5/hotel.csv"):
        with open(fname, "w", newline="") as f:
            wr = csv.writer(f)
            wr.writerow(["ID", "Type", "Price", "Status"])
            for rm in self.rms:
                wr.writerow([rm.rid, rm.rtype, rm.price, rm.booked])
        print("Data saved.")

    # Load hotel data from file
    def load_file(self, fname="DAY 5/hotel.csv"):
        try:
            with open(fname, "r") as f:
                rd = csv.reader(f)
                self.rms = []
                for row in rd:
                    rm = Room(row[0], row[1], float(row[2]))
                    rm.booked = row[3] == "True"
                    self.rms.append(rm)
            print("Data loaded.")
        except FileNotFoundError:
            print("No saved data.")



# Main program
ht = Hotel()    
ht.load_file()
while True:
    print("\n--- Hotel Menu ---")
    print("1. Add Room")
    print("2. View Rooms")
    print("3. Search Room by Type")
    print("4. Book Room by Type")
    print("5. Cancel Booking")
    print("6. Save & Exit")

    try:
        ch = int(input("Enter choice: "))
        if ch == 1:
            rid = input("Enter Room ID: ")
            rtype = input("Enter Room Type (1B/2B/3B/S): ")
            price = float(input("Enter Price: "))
            ht.add_room(rid, rtype, price)
        elif ch == 2:
            ht.view_rooms()
        elif ch == 3:
            rtype = input("Enter Room Type (1B/2B/3B/S): ")
            ht.search_room(rtype)
        elif ch == 4:
            rtype = input("Enter Room Type (1B/2B/3B/S): ")
            ht.book_room(rtype)
        elif ch == 5:
            rid = input("Enter Room ID to cancel: ")
            ht.cancel_book(rid)
        elif ch == 6:
            ht.save_file()
            print("Exit.")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Enter a valid number.")
