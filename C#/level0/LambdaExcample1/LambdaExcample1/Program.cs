namespace LambdaExcample1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            DoSomeCalc<int>((a, b) => { return a * b; }, 100, 200);
        }

        Func<int, int, int> func1 = new Func<int, int, int>(Add);
        static void DoSomeCalc<T>(Func<T,T,T>func,T x,T y)
        {
            T res = func(x, y);
            Console.WriteLine(res);
        }

        public static int Add(int x,int y)
        {
            int z = x + y;
            return z;
        }
    }
}
