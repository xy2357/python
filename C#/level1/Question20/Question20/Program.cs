using System.Net.Http.Headers;

namespace Question20
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
    }

    class Box
    {
        public Product Product { get; set; }
    }

    class Product
    {
        public string Name { get; set; }
    }

    class WrapFactory
    {
        public Box WrapProduct(Func<Product> getProduct)
        {
            Box box = new Box();
            Product product =
            box.Product = product;
            return box;
        }
    }
}
