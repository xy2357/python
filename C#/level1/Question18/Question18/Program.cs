namespace Question18
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Func<int, int, int> func = Add;

            Console.WriteLine(func.Invoke(10,20));
        }

        static int Add(int a, int b)
        {
            return a + b;
        }
    }
}
