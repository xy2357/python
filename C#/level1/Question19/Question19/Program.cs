namespace Question19
{
    class Program
    {
        static void Main(string[] args)
        {
            ProductFactory factory = new ProductFactory();
            //Func<Product> func = new Func<Product>(factory.MakePizza);
            Func<Product> func = factory.MakePizza;
            Product product = func();
            Console.WriteLine(product.Name);
        }
    }

    class Product
    {
        public string Name { get; set; }
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
}
