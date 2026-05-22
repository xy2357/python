using System.Data;

namespace EventSample3
{
    public delegate void Calc(int a, int b);

    internal class Program
    {
        static void Main(string[] args)
        {
            int x = 10;
            int y = 90;
            int z = 0;

            Calculater calculater = new Calculater();

            calculater.CalcEvent += calculater.Sub;
            calculater.CalcEvent += calculater.Mul;
            calculater.CalcEvent += calculater.Div;

            calculater.Add(x, y);
        }
    }

    class Calculater
    {
        public event Calc? CalcEvent;

        public void Add(int a, int b)
        {
            Console.WriteLine($"Add:{a + b}");

            CalcEvent?.Invoke(a, b);
        }
        public void Sub(int a, int b)
        {
            Console.WriteLine($"Sub:{a - b}");
        }
        public void Mul(int a, int b)
        {
            Console.WriteLine($"Mul:{a * b}");
        }
        public void Div(int a, int b)
        {
            Console.WriteLine($"Div:{a / b}");
        }
    }
}
