namespace MethodOverriding;

public class BankAccount
{
    public double Balance { get; set; }

    public BankAccount(double balance)
    {
        Balance = balance;
    }

    public virtual double CalculateInterest()
    {
        return Balance * 0.03;
    }
}