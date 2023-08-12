class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def main():
    # Creating instances (objects) of the Person class
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)

    # Accessing object attributes
    print("Person 1 - Name:", person1.name, "Age:", person1.age)
    print("Person 2 - Name:", person2.name, "Age:", person2.age)

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()
