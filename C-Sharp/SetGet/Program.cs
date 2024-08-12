using System;

public class Person
{
    private string name;

    // Public property with get and set accessors
    public string Name
    {
        get
        {
            return name;
        }
        
        set
        {
            if (!string.IsNullOrWhiteSpace(value))
            {
                name = value;
            }
            else
            {
                Console.WriteLine("Name cannot be empty.");
            }
            
        }
    }
}

public class Program
{
    public static void Main()
    {
        Person person = new Person();
        
        person.Name = "Imam Hossain Roni";
        Console.WriteLine($"Perspn's name is: {person.Name}");
        
        person.Name = "";
        Console.WriteLine($"Perspn's name is: {person.Name}");

    }
}