namespace Question10
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, int> prices = new Dictionary<string, int>();

            prices.Add("Pizza", 30);
            prices.Add("Book", 50);
            prices.Add("ToyCar", 100);

            if (prices.TryGetValue("Book", out int price))
            {
                Console.WriteLine(price);
            }
            else
            {
                Console.WriteLine("Not found Phone!");
            }
        }
    }
}
