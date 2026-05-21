namespace Question14
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<Product> products = new List<Product>();

            Product product1 = new Product();
            product1.Name = "Pizza";
            product1.Price = 30;
            Product product2 = new Product();
            product2.Name = "Book";
            product2.Price = 50;
            Product product3 = new Product();
            product3.Name = "ToyCar";
            product3.Price = 100;

            products.Add(product1);
            products.Add(product2);
            products.Add(product3);

            foreach (Product product in products)
            {
                Console.WriteLine("{0}:{1}", product.Name, product.Price);
            }
        }

        class Product
        {
            public string Name { get; set; }
            public int Price { get; set; }
        }
    }
}
