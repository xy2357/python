namespace Question3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int x = 5;

            Console.WriteLine(x++); //先用，再加
            Console.WriteLine(++x); //先加，再用
            Console.WriteLine(x);
        }
    }
}
