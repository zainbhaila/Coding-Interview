/*
Zain Bhaila
03/05/2020
HW5: Inheritance
*/
/*
Question 1: Is this an online banking system or brick-and-mortar, or some combination of the two? Does it have
physical ATM locations and ways to deposit cash.
Answer: Online banking system, similiar to Ally or Charles Schwab. No physical ATMs or cash deposits, but can
withdraw cash from other companys' ATMs with any applicable fees.
*/
/*
Question 2: What kind of accounts does this bank offer? Checkings, savings, brokerage, CD, etc?
Answer: Only checkings and savings accounts.
*/
/*
Question 3: Is this bank a regional bank covering a small area or is it a larger/nationwide bank?
Answer: We can say it is a smaller bank, servicing a few states.
*/

public class Bank {
    Customers[] cust;
    Accounts[] accounts;
    
    public Bank() {} // create the bank
    
    public void addCustomer(Customer c) {} // add a customer to the bank
    public void notifyAll(int priority) {} // send a notification to all customers
    public void financialCrisis() {} // request government for a bailout
}

public abstract class Account {
    String accountNumber; // account number
    Customer accountHolder; // who owns the account
    Customer[] authorizedUsers; // who has access to the account
    float minimumBalance; // minimum balance to keep account open
    float accountBalance; 
    
    public void deposit(float amount) {} // deposit money into account
    public abstract void withdraw(float amount); // withdraw money from account
    public abstract void closeAccount(); // different procedures for different account types
    public void transferMoney(float amount, String transferToNumber) {} // transfer money between accounts
    public void addUser(Customer user) {} // add a authorized user
    public void removeUser(Customer user) {} // remove a authorized user
}

public class Savings extends Account {
    float interestRate; // interest earnings
    int weeklyWithdrawalLimit; // access frequency
    
    public Savings(String n, String h, float min, float interest, int lim) {} // open a savings account
    
    public void withdraw(float amount) {} // withdrawals are limited for savings accounts
    public void closeAccount() {}
}

public class Checking extends Account {
    float overdraftPenalty; // amount charged for overdrafts
    String routingNumber; // for direct deposit/withdrawal
    DebitCard[] cards; // all cards linked to this account
    
    public Checking(String n, String h, float min, float over, String route) {} // open a checking account
    
    public void autoPay() {} // pay bills automatically
    public void payment(float amount) {} // make a payment from the account
    public void closeAccount() {} // must also unlink any debit cards
    public void withdraw(float amount) {}
    public void addCard(String cardNumber) {} // add a new card to the account
    public void cancelCard(String cardNumber) {} // cancel a debit card
}

public class Customer {
    String name; // customer's name
    Date birthdate;
    String ssn;
    String address;
    String email;
    Date lastUpdated;
    
    public Customer(String n, Date b, String s, String a, String e) {} // create a new customer
    
    public void updateInfo(String ad, String e, Date l) {} // update a customer's info
    public void notifyCustomer(String message) {} // send a message to a customer
    public void openAccount(Account a) {} // create and link a customet to an account
    public void closeAccounts(Account[] a) {} // close accounts related to customer

public class DebitCard {
    public enum Provider {
        VISA("VISA"), DISCOVER("DISCOVER"), MASTERCARD("MASTERCARD"), AMEX("American Express");
    }
    
    String number; // credit card number
    int cvv; // that three digit number on the back of the card
    int pin; // four digit security pin
    Date expiration; // card expiration date
    Customer holder; // name on the card
    Provider prov; // the card service provider
    
    public DebitCard(String n, int c, int p, Date e, Customer h, Provider p) {} // instantiate the debit card with values
    
    public void authorizeTransaction() {} // make a payment with the card
    public void linkAccount() {} // link card to an external payment account (i.e. Google Pay, Paypal)
    public void cancelCard() {} // cancel the card
}