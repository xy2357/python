namespace Question12
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string,int> products = new Dictionary<string,int>();

            products.Add("Pizza", 30);
            products.Add("ToyCar", 100);

            if (products.ContainsKey("Pizza"))
            {
                Console.WriteLine(products["Pizza"]);
            }
            else
            {
                Console.WriteLine("Pizza is not in Dictionary!");
            }
        }
    }
}
