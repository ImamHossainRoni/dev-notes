using System;

public class BankAccount
{
    // Private field to store the balance
    private decimal balance;

    public void Deposit(decimal amount)
    {
        if (amount > 0)
        {
            balance += amount;
            Console.WriteLine($"Deposited: ${amount}. New balance: ${balance}");
        }
        else
        {
            Console.WriteLine("Deposit amount must be positive.");
        }
    }

    public void Withdraw(decimal amount)
    {
        if (amount > 0)
        {
            if (amount <= balance)
            {
                balance -= amount;
                Console.WriteLine($"Withdrew: ${amount}. New balance: ${balance}");
            }
            else
            {
                Console.WriteLine("Withdrawal amount must be positive.");
            }
        }
    }

    public decimal GetBalance()
    {
        return balance;
    }

    
}

public class Program
{
    public static void Main()
    {
        BankAccount account = new BankAccount();
        account.Deposit(1000);
        account.Withdraw(300);
        Console.WriteLine($"Current balance: ${account.GetBalance()}");
    }
}