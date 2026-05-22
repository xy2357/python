namespace SimpleEvent
{
    public delegate void Notify();

    internal class Program
    {
        static void Main(string[] args)
        {
            Boss boss = new Boss();

            Boy boy = new Boy();
            Girl girl = new Girl();

            boss.WorkOver += boy.GoHome;
            boss.WorkOver += girl.GoHome;

            boss.SayWorkOver();
        }
    }

    class Boss
    {
        public event Notify? WorkOver;

        public void SayWorkOver()
        {
            Console.WriteLine("老板说：下班了！");

            WorkOver?.Invoke();
        }
    }

    class Boy
    {
        public void GoHome()
        {
            Console.WriteLine("男孩回家");
        }
    }

    class Girl
    {
        public void GoHome()
        {
            Console.WriteLine("女孩回家");
        }
    }
}
