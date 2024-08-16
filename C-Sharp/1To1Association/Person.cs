namespace _1To1Association;

public class Person
{
    public string FirstName { get; set; }
    public string LastName { get; set; }
    public Address PermanentAddress { get; set; }
    public string GetFullName()
    {
        return FirstName + " " + LastName;
    }
}