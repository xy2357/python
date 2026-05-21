namespace Question4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int score = 55;

            if (score >= 90)
            {
                Console.WriteLine("A");
            }
            else if(score >= 80)
            {
                Console.WriteLine("B");
            }
            else if (score >= 60)
            {
                Console.WriteLine("C");
            }
            else
            {
                Console.WriteLine("D");
            }
        }
    }
}
