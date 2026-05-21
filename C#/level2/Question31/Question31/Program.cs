namespace Question31
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ProductFactory productfactory = new ProductFactory();
            WrapFactory wrapFactory = new WrapFactory();
            Box box1 = wrapFactory.WrapProduct(productfactory.MakePizza);
            Box box2 = wrapFactory.WrapProduct(productfactory.MakeBook);

            Console.WriteLine("{0}:{1}", box1.Product.Name, box1.Product.Price);
            Console.WriteLine("{0}:{1}", box2.Product.Name, box2.Product.Price);
        }
    }

    class Product
    {
        public string Name { get; set; }
        public int Price { get; set; }
    }

    class Box
    {
        public Product Product { get; set; }
    }

    class ProductFactory
    {
        public Product MakePizza()
        {
            Product product = new Product();
            product.Name = "Pizza";
            product.Price = 30;
            return product;
        }

        public Product MakeBook()
        {
            Product product = new Product();
            product.Name = "Book";
            product.Price = 50;
            return product;
        }
    }

    class WrapFactory
    {
        public Box WrapProduct(Func<Product> getProduct)
        {
            Box box = new Box();
            Product product = getProduct();
            box.Product = product;
            return box;
        }
    }
}
