class Product
{
    public string Name { get; set; }
    public decimal Price { get; set; }

    public Product(string name, decimal price)
    {
        Name = name;
        Price = price;
    }
    
    public Product(string name)
    {
        Name = name;
    }

}

class Program
{
    public static void Main()
    {
        Product product1 = new Product("iPhone 15 Pro Max", 1199);
        Product product2= new Product("iPhone 15 Pro Max");
        Console.WriteLine($"Product Name : {product1.Name} and Price {product1.Price}");
        Console.WriteLine($"Product Name : {product1.Name}");
    }
}