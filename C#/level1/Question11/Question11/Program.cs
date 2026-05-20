using System.Security.Cryptography.X509Certificates;

namespace Question11
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string,int> products = new Dictionary<string,int>();

            products.Add("Pizza", 30);
            products.Add("ToyCar", 100);
            products.Add("Book", 50);

            foreach (var product in products)
            {
                Console.WriteLine("{0}:{1}",product.Key,product.Value);
            }
        }
    }
}
