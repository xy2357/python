using System.Threading.Channels;

namespace Question15
{
    internal class Program
    {
        static void Main(string[] args)
        {
            object o = new Teacher();

            Console.WriteLine(o.GetType().Name);
        }

        class Teacher
        {
            public void Teach()
            {
                Console.WriteLine("Teach");
            }
        }
    }
}
