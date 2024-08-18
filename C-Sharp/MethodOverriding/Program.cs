using MethodOverriding;

class Program
{
    public static void Main()
    {
        BankAccount generalAccount = new BankAccount(1000);
        SavingsAccount savingsAccount = new SavingsAccount(1000);
        CurrentAccount currentAccount = new CurrentAccount(1000);
        
        Console.WriteLine("General Account Interest: " + generalAccount.CalculateInterest());
        Console.WriteLine("Savings Account Interest: " + savingsAccount.CalculateInterest());
        Console.WriteLine("Current Account Interest: " + currentAccount.CalculateInterest());
        
    }
}