namespace Question12
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Student stu = new Student("Small Li", 20);
            Console.WriteLine("{0} age is {1}", stu.Name, stu.Age);
        }
    }

    class Student(string name, int age)
    {
        public string Name { get { return name; } }
        public int Age { get { return age; } }
    }
}
