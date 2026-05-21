namespace Question20
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ProductFactory productFactory = new ProductFactory();
            WrapFactory wrapFactory = new WrapFactory();

            Func<Product> func = productFactory.MakePizza;

            Box box = wrapFactory.WrapProduct(func);

            Console.WriteLine(box.Product.Name);
        }
    }

    class Product
    {
        public string Name { get; set; }
    }

    class Box
    {
        public Product Product { get; set; }
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

    class WrapFactory
    {
        public Box WrapProduct(Func<Product> getProduct)
        {
            Box box = new Box();

            Product product = getProduct.Invoke();

            box.Product = product;

            return box;
        }
    }
}