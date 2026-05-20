namespace Question14
{
    internal class Program
    {
        static void Main(string[] args)
        {
            object o = new Teacher();
            Teacher t = o as Teacher;

            if (t != null)
            {
                t.Teach();
            }
            else
            {
                Console.WriteLine("I am not a teacher!");
            }

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
