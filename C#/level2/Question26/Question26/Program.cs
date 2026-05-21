namespace Question26
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Func<int> fun = new Func<int>(GetNumber);
            int a = fun();
            Console.WriteLine(a);
        }

        static int GetNumber()
        {
            return 100;
        }
    }
}
