namespace Question15
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<Product> products = new List<Product>();

            products.Add(new Product { Name = "Pizza", Price = 30 });
            products.Add(new Product { Name = "Book", Price = 50 });
            products.Add(new Product { Name = "ToyCar", Price = 100 });

            int sum = 0;

            foreach (Product product in products)
            {
                sum += product.Price;
            }

            Console.WriteLine("Total price : {0}", sum);
        }

        class Product
        {
            public string Name { get; set; }
            public int Price { get; set; }
        }
    }
}

