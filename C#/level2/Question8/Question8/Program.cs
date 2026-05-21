namespace Question8
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<string> names = new List<string>();

            names.Add("Alice");
            names.Add("Bob");
            names.Add("Cindy");
            names.Add("David");


            if (names.Contains("Bob"))
            {
                Console.WriteLine("Bob exists!");
            }
            else
            {
                Console.WriteLine("Bob not found!");
            }
        }
    }
}
