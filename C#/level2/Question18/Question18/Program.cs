namespace Question18
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Calc(9, 4,out int sum, out int diff);
            Console.WriteLine("sum:{0}\ndiff:{1}", sum, diff);
        }

        static void Calc(int x, int y, out int sum, out int diff)
        {
            sum = x + y;
            diff = y - x;
        }
    }
}
