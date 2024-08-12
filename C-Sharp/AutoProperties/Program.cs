using System;

class Person
{ 
    public string Name { get; set; }
    
    public Person(string name)
    {
        Name = name;
    }
}

public class Program
{
    public static void Main()
    {
        Person person = new Person("Imam Hossain Roni");
        Console.WriteLine($"Person's name is : {person.Name}");
        
    }
}