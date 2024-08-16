
using _1To1Association;

class Program
{
    public static void Main()
    {
        Address address = new Address();
        address.HouseNo = "H-10";
        address.RoadNo = "07";
        address.Area = "South Banasree";
        address.District = "Dhaka";
        address.PostCode = "1219";
        
        Person person1 = new Person();
        
        person1.FirstName = "Imam Hossain";
        person1.LastName = "Roni";
        person1.PermanentAddress = address;
        
        
        Console.WriteLine($"Name : {person1.GetFullName()}");
        Console.WriteLine($"Address : {person1.PermanentAddress.GetFullAddress()}");
    }
}