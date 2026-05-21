namespace Question32
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<Product> products = new List<Product>();
            products.Add(new Product { Name = "Pizza", Price = 30 });
            products.Add(new Product { Name = "Book", Price = 50 });
            products.Add(new Product { Name = "ToyCar", Price = 100 });
            products.Add(new Product { Name = "Pen", Price = 5 });

            foreach (Product product in products)
            {
                if (product.Price >= 50)
                {
                    Console.WriteLine("{0}: {1}", product.Name, product.Price);
                }
            }
        }
    }

    class Product
    {
        public string Name { get; set; }
        public int Price { get; set; }
    }
}
