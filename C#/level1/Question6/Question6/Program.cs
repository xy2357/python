namespace Question6
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Person p = new Person();
            p.Name = "Alice";

            Change(p);

            Console.WriteLine(p.Name);
        }

        class Person
        {
            public string Name { get; set; }
        }

        static void Change(Person p)
        {
            p = new Person();
            p.Name = "Bob";
        }
    }
}
