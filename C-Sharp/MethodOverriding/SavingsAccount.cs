namespace MethodOverriding;

class SavingsAccount : BankAccount
{
    public SavingsAccount(double balance) : base(balance){}

    public override double CalculateInterest()
    {
        return Balance * 0.05;
    }
    
}

class CurrentAccount : BankAccount
{
    public CurrentAccount(double balance) : base(balance){}
    
    public override double CalculateInterest()
    {
        return Balance * 0.01;
    }
}