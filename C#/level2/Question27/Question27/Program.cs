namespace Question27
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Func<int, int, int> func = new Func<int, int, int>(Add);

            Console.WriteLine(func(10, 20));
        }

        static int Add(int a,int b)
        {
            return a + b;
        }
    }
}
