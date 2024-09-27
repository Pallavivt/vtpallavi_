class FitnessClass:
    def _init_(self, name, instructor, date, time, duration, capacity):
        self.name = name
        self.instructor = instructor
        self.date = date
        self.time = time
        self.duration = duration
        self.capacity = capacity
        self.bookings = []

    def is_full(self):
        return len(self.bookings) >= self.capacity

class BookingSystem:
    def _init_(self):
        self.classes = []
        self.user_bookings = {}

    def add_class(self):
        name = input("Enter class name: ")
        instructor = input("Enter instructor name: ")
        date = input("Enter date (YYYY-MM-DD): ")
        time = input("Enter time (HH:MM AM/PM): ")
        duration = input("Enter duration (e.g., 1 hour): ")
        capacity = int(input("Enter capacity: "))
        fitness_class = FitnessClass(name, instructor, date, time, duration, capacity)
        self.classes.append(fitness_class)
        print(f"Class '{name}' added successfully!")

    def view_classes(self):
        if not self.classes:
            print("No classes available.")
            return
        print("Available Classes:")
        for idx, fitness_class in enumerate(self.classes):
            status = "Full" if fitness_class.is_full() else f"Available spots: {fitness_class.capacity - len(fitness_class.bookings)}"
            print(f"{idx + 1}. {fitness_class.name} - Instructor: {fitness_class.instructor}, Date: {fitness_class.date}, Time: {fitness_class.time}, Duration: {fitness_class.duration}, {status}")

    def book_class(self):
        self.view_classes()
        class_id = int(input("Enter the class number you want to book: ")) - 1
        if class_id < 0 or class_id >= len(self.classes):
            print("Invalid class number.")
            return
        fitness_class = self.classes[class_id]
        if fitness_class.is_full():
            print("Class is full, cannot book.")
            return
        user_name = input("Enter your name: ")
        fitness_class.bookings.append(user_name)
        if user_name not in self.user_bookings:
            self.user_bookings[user_name] = []
        self.user_bookings[user_name].append(fitness_class)
        print(f"You have successfully booked '{fitness_class.name}'!")

    def view_your_bookings(self):
        user_name = input("Enter your name: ")
        bookings = self.user_bookings.get(user_name, [])
        if not bookings:
            print("No bookings found for you.")
            return
        print("Your Bookings:")
        for booking in bookings:
            print(f"{booking.name} - Date: {booking.date}, Time: {booking.time}")

    def update_booking(self):
        user_name = input("Enter your name: ")
        bookings = self.user_bookings.get(user_name, [])
        if not bookings:
            print("No bookings found for you.")
            return
        self.view_your_bookings()
        booking_index = int(input("Enter the booking number to update: ")) - 1
        if booking_index < 0 or booking_index >= len(bookings):
            print("Invalid booking number.")
            return
        old_class = bookings[booking_index]
        self.classes.append(old_class)  # Re-add the old class for available classes
        self.view_classes()
        new_class_id = int(input("Enter the new class number: ")) - 1
        if new_class_id < 0 or new_class_id >= len(self.classes):
            print("Invalid class number.")
            return
        new_class = self.classes[new_class_id]
        if new_class.is_full():
            print("New class is full, cannot update booking.")
            return
        self.user_bookings[user_name].remove(old_class)
        new_class.bookings.append(user_name)
        self.user_bookings[user_name].append(new_class)
        print(f"Your booking has been updated to '{new_class.name}'!")

    def cancel_booking(self):
        user_name = input("Enter your name: ")
        bookings = self.user_bookings.get(user_name, [])
        if not bookings:
            print("No bookings found for you.")
            return
        self.view_your_bookings()
        booking_index = int(input("Enter the booking number to cancel: ")) - 1
        if booking_index < 0 or booking_index >= len(bookings):
            print("Invalid booking number.")
            return
        canceled_class = bookings[booking_index]
        canceled_class.bookings.remove(user_name)
        self.user_bookings[user_name].remove(canceled_class)
        print(f"Your booking for '{canceled_class.name}' has been canceled.")

def main():
    system = BookingSystem()
    while True:
        print("\nFitness Class Booking System")
        print("1. Add Fitness Class")
        print("2. View Available Classes")
        print("3. Book a Class")
        print("4. View Your Booking")
        print("5. Update Your Booking")
        print("6. Cancel Your Booking")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            system.add_class()
        elif choice == '2':
            system.view_classes()
        elif choice == '3':
            system.book_class()
        elif choice == '4':
            system.view_your_bookings()
        elif choice == '5':
            system.update_booking()
        elif choice == '6':
            system.cancel_booking()
        elif choice == '7':
            print("Thank you for using the Fitness Class Booking System! Have a great day!")
            break
        else:
            print("Invalid option, please try again.")

if __name__== "_main_":
    main()