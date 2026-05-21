namespace Question30
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Action<string> action = new Action<string>(PrintName);
            action("Small Li");
        }
        static void PrintName(string name)
        {
            Console.WriteLine(name);
        }
    }
}
