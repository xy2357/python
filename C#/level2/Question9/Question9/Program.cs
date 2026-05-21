namespace Question9
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, int> prices = new Dictionary<string, int>();

            prices.Add("Pizza", 30);
            prices.Add("Book", 50);
            prices.Add("ToyCar", 100);

            foreach (string product in prices.Keys)
            {
                Console.WriteLine("{0} cost {1}", product, prices[product]);
            }
        }
    }
}
