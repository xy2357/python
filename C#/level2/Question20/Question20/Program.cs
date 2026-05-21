namespace Question20
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Player p = new Player();
            p.Name = "Alice";
            Change(p);
            Console.WriteLine(p.Name);
        }

        class Player
        {
            private string name;

            public string Name
            {
                get
                {
                    return name;
                }
                set
                {
                    name = value;
                }
            }
        }

        static void Change(Player p)
        {
            p.Name = "Bob";
        }
    }
}
