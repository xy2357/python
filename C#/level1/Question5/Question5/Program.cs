namespace Question5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Person person = new Person();
            person.Name = "Alice";

            Change(person);

            Console.WriteLine(person.Name);
        }

        static void Change(Person p)
        {
            p.Name = "Bob";
        }

        class Person
        {
            public string Name { get; set; }
        }

    }
}
