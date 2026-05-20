namespace Question9
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Product[] products = new Product[3];

            products[0] = new Product();
            products[0].Name = "Pizza";
            products[0].Price = 30;
            products[1] = new Product();
            products[1].Name = "ToyCar";
            products[1].Price = 100;
            products[2] = new Product();
            products[2].Name = "Book";
            products[2].Price = 50;

            foreach (var product in products)
            {
                Console.WriteLine("{0}:{1}", product.Name,product.Price);
            }

        }

        class Product
        {
            public string Name {  get; set; }
            public int Price { get; set; }
        }

    }
}
