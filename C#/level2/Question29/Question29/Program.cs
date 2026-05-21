namespace Question29
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Action action = SayHello;
            action.Invoke();
        }

        static void SayHello()
        {
            Console.WriteLine("Hello");
        }
    }
}
