namespace Question13
{
    internal class Program
    {
        static void Main(string[] args)
        {
            object o = "hello";

            if (o is string)
            {
                string s = (string)o;

                Console.WriteLine(s.Length);
            }
        }
    }
}
