namespace DelegateEventSample
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Publisher publisher = new Publisher();
            Subscriber subscriber = new Subscriber();

            publisher.SomethingHappened += subscriber.OnSomethingHappened;

            publisher.DoSomething();
        }
    }

    class Publisher
    {
        public delegate void MyEventHandle(string message);

        public event MyEventHandle? SomethingHappened;

        public void DoSomething()
        {
            Console.WriteLine("事情发生了！");

            SomethingHappened?.Invoke("通知：事情发生了");
        }
    }

    class Subscriber
    {
        public void OnSomethingHappened(string message)
        {
            Console.WriteLine(message);
        }
    }
}
