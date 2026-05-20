namespace Quesstion7
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Product product1 = new Product();
            Product product2 = new Product();

            product1.Name = "Pizza";
            product1.Price = 30;
            product2.Name = "Toycat";
            product2.Price = 100;

            Console.WriteLine("{0}:{1}", product1.Name, product1.Price);
            Console.WriteLine("{0}:{1}", product2.Name, product2.Price);

        }

        class Product
        { 
            public string Name { get; set; }
            public int Price { get; set; }
        }

    }
}
