namespace Object_Class;

class Person
{
    public string firstName;
    public string middleName;
    public string lastName;

    public string GetFullName()
    {
        string fullName = firstName + ' ' + middleName + ' ' + lastName;
        return fullName;
    }
}