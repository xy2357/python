namespace Question7
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

            foreach (string name in names)
            {
                Console.WriteLine(name);
            }
        }
    }
}
