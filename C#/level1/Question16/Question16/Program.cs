namespace Question16
{
    internal class Program
    {


        static void Main(string[] args)
        {
            Func<int> func = GetNumber;
            int a = func.Invoke();
            Console.WriteLine(a);
        }

        static int GetNumber()
        {
            return 100;
        }
    }
}
