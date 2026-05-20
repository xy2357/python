namespace Question4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int a = 10;
            Change(a);
            Console.WriteLine(a);//打印a=10
        }

        static void Change(int x)
        {
            x = 100;
        }
    }
}
