namespace Question28
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ProductFactory factory = new ProductFactory();
            Func<Product> func = new Func<Product>(factory.MakePizza);
            Product p = func();
            Console.WriteLine(p.Name);
        }

        class ProductFactory
        {
            public Product MakePizza()
            {
                Product p = new Product();
                p.Name = "Pizza";
                return p;
            }
        }

        class Product
        {
            public string Name { get; set; }
        }


    }
}
