namespace Question35
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string text = "hello world";

            string text1 = text.Trim();
            Console.WriteLine(text1);

            string text2 = text.ToUpper();
            Console.WriteLine(text2);

            int text3 = text.Length;
            Console.WriteLine(text3);
        }
    }
}
