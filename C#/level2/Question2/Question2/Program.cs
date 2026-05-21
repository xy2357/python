namespace Question2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string s1 = "hello";
            string s2 = s1;
            s2 = "world";

            Console.WriteLine(s1);
            Console.WriteLine(s2);
        }
    }
}
