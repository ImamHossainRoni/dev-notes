namespace MethodOverloading;

public class PaymentProcessor
{
    public void ProcessPayment(string cardNumber, string cardHolder, string expiryDate, string cvv)
    {
        Console.WriteLine("Processing credit card payment...");

    }

    public void ProcessPayment(string bankAccountNumber, string bankName)
    {
        Console.WriteLine("Processing bank transfer payment.....");
    }

    public void ProcessPayment(string walletId, double amount)
    {
        Console.WriteLine("Processing digital wallet payment.....");
    }

    public void ProcessPayment(string cardNumber, string cardHolder, string expiryDate, string cvv, string discountCode)
    {
        Console.WriteLine("Processing credit card payment with a discount code...");

    }
}