namespace Question19
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int a = 10;
            Change(a);
            Console.WriteLine(a);
        }

        static void Change(int x)
        {
            x = 100;
        }
    }
}
