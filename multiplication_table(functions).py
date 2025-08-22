def create_table(number, limit=15):
    """Prints the multiplication table of a number up to a given limit"""
    print(f"\nMultiplication Table for {number}\n")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

def main():
    """Main function to run the program"""
    try:
        number = int(input("Enter number to create multiplication table: "))
        create_table(number, 15)
    except ValueError:
        print("Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()
