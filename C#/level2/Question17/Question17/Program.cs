namespace Question17
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var result = Calc(10, 20);
            Console.WriteLine(result.Item1);
            Console.WriteLine(result.Item2);
        }

        static (int, int) Calc(int x, int y)
        {
            return (x + y, x - y);
        }
    }
}
