using MethodOverloading;

class Program
{
    public static void Main()
    {
        PaymentProcessor paymentProcessor = new PaymentProcessor();
        // Process a credit card payment
        paymentProcessor.ProcessPayment("1234-5678-9012-3456", "John Doe", "12/25", "123");

        // Process a bank transfer payment
        paymentProcessor.ProcessPayment("9876543210", "National Bank");

        // Process a digital wallet payment
        paymentProcessor.ProcessPayment("wallet123", 100.50);

        // Process a credit card payment with a discount code
        paymentProcessor.ProcessPayment("1234-5678-9012-3456", "John Doe", "12/25", "123", "DISCOUNT20");
    }
}