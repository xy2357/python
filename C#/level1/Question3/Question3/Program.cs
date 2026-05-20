namespace Question3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Student stu = new Student();
            stu.Name = "Small Li";
            stu.Age = 18;

            Console.WriteLine(stu.Name);
            Console.WriteLine(stu.Age);
        }
    }

    class Student
    {
        //public string name;
        //public int age;

        public string Name { get; set; }
        public int Age {  get; set; }
    }
}
