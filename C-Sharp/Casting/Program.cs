class Animal
{
    public void Eat()
    {
        Console.WriteLine("Animal is eating");
    }
}

class Dog : Animal
{
    public void Bark()
    {
        Console.WriteLine("Dog is barking");
    }
}
class Program
{
    public static void Main()
    {
        // Dog dog = new Dog();
        // Animal animal = dog; // Upcasting
        // animal.Eat(); // This works
      // animal.Bark(); // This won't work because Animal doesn't have the Bark method

      Animal animal = new Animal(); // Upcasting
      Dog dog = (Dog)animal;  // Downcasting
      dog.Bark();  // Now we can call Bark, which isn't available in Animal

    }
}
