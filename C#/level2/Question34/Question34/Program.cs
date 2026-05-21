namespace Question34
{
    internal class Program
    {
        static void Main(string[] args)
        {
			int a = 10;
			int b = 0;
			try
			{
				int result = a / b;
			}
			catch (Exception ex)
			{
                Console.WriteLine(ex.Message);
			}
        }
    }
}
