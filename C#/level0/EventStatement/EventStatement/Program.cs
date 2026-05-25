using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Security.Policy;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace EventStatement
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Customer customer = new Customer();
            Waiter waiter = new Waiter();
            customer.Order += waiter.Action;
            customer.Action();
            customer.PayTheBill();
        }
    }

    public class OrderEventArgs:EventArgs
    {
        public string DishName {  get; set; }
        public string Size {  get; set; }
    }

    public delegate void OrderEventHandler(Customer customer, OrderEventArgs e);

    public class Customer
    {

        //public OrderEventHandler orderEventHandler;

        //public event OrderEventHandler Order
        //{
        //    add
        //    {
        //        orderEventHandler += value;
        //    }
        //    remove
        //    {
        //        orderEventHandler -= value;
        //    }
        //}

        public event OrderEventHandler Order;

        public double Bill { get; set; }
        
        public void PayTheBill()
        {
            Console.WriteLine($"I will pay ${this.Bill}");
        }

        public void WalkIn()
        {
            Console.WriteLine("Walk into the restaurant");
        }

        public void SitDown()
        {
            Console.WriteLine("Sit Down");
        }

        public void Think()
        {
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine("Thinking...");
                Thread.Sleep(1000);
            }

            if (this.Order != null)
            {
                OrderEventArgs e = new OrderEventArgs();
                e.DishName = "Buger";
                e.Size = "large";
                this.Order(this, e);
            }
        }

        public void Action()
        {
            Console.ReadLine();
            this.WalkIn();
            this.SitDown();
            this.Think();
        }
    }

    public class Waiter
    {
        public void Action(Customer customer, OrderEventArgs e)
        {
            Console.WriteLine($"I will serve you ths dish - {e.DishName}");
            double price = 10;
            switch (e.Size)
            {
                case "small":
                    price = price * 0.5;
                    break;
                case "large":
                    price = price * 1;
                    break;
                default:
                    break;
            }
            customer.Bill += price;
        }
    }
}
