namespace Question13
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
    }

    class Player
    {

        private string name;
        private int level;

        public string Name
        {
            get
            {
                return name;
            }
        }

        public int Level
        {
            get
            {
                return level;
            }
            set
            {
                level = value;
            }
        }
    }
}
