
public class DogDemo {

    // Dog class definition
    static class Dog {
        // Class variable (shared by all Dog objects)
        static String species = "Canis lupus familiaris";

        // Instance variables (unique to each Dog object)
        private String name;
        private String breed;

        // Constructor to initialize instance variables
        public Dog(String name, String breed) {
            if (name == null || name.isEmpty() || breed == null || breed.isEmpty()) {
                throw new IllegalArgumentException("Name and breed must not be empty.");
            }
            this.name = name;
            this.breed = breed;
        }

        // Method to display dog details
        public void displayDetails() {
            System.out.println("Name: " + name);
            System.out.println("Breed: " + breed);
            System.out.println("Species: " + species);
            System.out.println("----------------------");
        }
    }

    // Main method to run the program
    public static void main(String[] args) {
        try {
            // Create two Dog objects with different breeds
            Dog dog1 = new Dog("Buddy", "Golden Retriever");
            Dog dog2 = new Dog("Max", "German Shepherd");

            // Display details of each dog
            System.out.println("Dog 1 Details:");
            dog1.displayDetails();

            System.out.println("Dog 2 Details:");
            dog2.displayDetails();

        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
