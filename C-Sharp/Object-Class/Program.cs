using Object_Class;

class Program 
{
    string color = "red";

    static void Main(string[] args)
    {
        Person person1 = new Person();
        person1.firstName = "Imam";
        person1.middleName = "Hossain";
        person1.lastName = "Roni";
        Console.WriteLine(person1.GetFullName());
    }
}