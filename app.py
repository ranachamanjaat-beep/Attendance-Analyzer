import csv
import os

FILE_NAME = "data.csv"
REQUIRED_PERCENT = 75


# Initialize CSV file
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Total Classes", "Attended Classes"])


# Save data
def save_data(total, attended):
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([total, attended])


# Load last record
def load_last_record():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = list(csv.reader(file))
            if len(reader) > 1:
                last = reader[-1]
                return int(last[0]), int(last[1])
    except:
        pass
    return 0, 0


# Calculate attendance percentage
def calculate_percentage(total, attended):
    if total == 0:
        return 0
    return (attended / total) * 100


# Calculate bunkable classes
def calculate_bunk(total, attended):
    bunk = 0
    while True:
        if calculate_percentage(total + bunk, attended) >= REQUIRED_PERCENT:
            bunk += 1
        else:
            break
    return bunk - 1


# Calculate required classes to attend
def calculate_required(total, attended):
    required = 0
    while calculate_percentage(total + required, attended + required) < REQUIRED_PERCENT:
        required += 1
    return required


# Display menu
def menu():
    print("\n📊 Smart Attendance Analyzer")
    print("1. Add New Record")
    print("2. View Analysis")
    print("3. Exit")


def main():
    initialize_file()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            total = int(input("Enter total classes: "))
            attended = int(input("Enter attended classes: "))

            if attended > total:
                print("❌ Attended classes cannot be more than total classes.")
                continue

            save_data(total, attended)
            print("✅ Data saved successfully!")

        elif choice == '2':
            total, attended = load_last_record()

            if total == 0:
                print("⚠️ No data found. Please add records first.")
                continue

            percentage = calculate_percentage(total, attended)
            bunk = calculate_bunk(total, attended)
            required = calculate_required(total, attended)

            print("\n📈 Attendance Summary:")
            print(f"Total Classes: {total}")
            print(f"Attended Classes: {attended}")
            print(f"Attendance: {percentage:.2f}%")

            if percentage >= REQUIRED_PERCENT:
                print(f"😎 You can bunk {bunk} classes safely.")
            else:
                print(f"📚 You need to attend {required} more classes to reach {REQUIRED_PERCENT}%.")

        elif choice == '3':
            print("👋 Exiting program.")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()