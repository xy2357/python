namespace Question11
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Student student = new Student();
            student.Name = "Small Li";
            student.Age = 18;

            Console.WriteLine("{0} is {1} years old", student.Name, student.Age);
        }

        class Student
        {
            public int Age { get; set; }
            public string Name { get; set; }

        }
    }
}
