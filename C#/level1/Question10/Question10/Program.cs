namespace Question10
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<string> names = new List<string>();
            names.Add("Alice");
            names.Add("Bob");
            names.Add("Tom");

            foreach (var name in names)
            {
                Console.WriteLine(name);
            }
        }
    }
}
