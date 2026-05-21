namespace Question6
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] array = { 10, 20, 30, 40, 50 };
            int sum = 0;
            foreach (int num in array)
            {
                sum += num;
            }
            Console.WriteLine(sum);
        }
    }
}
