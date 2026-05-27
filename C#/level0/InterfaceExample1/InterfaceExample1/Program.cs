using System.Collections;

namespace InterfaceExample1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var user = new PhoneUser(new NokiaPhone());
            user.UserPhone();
        }
    }

    class PhoneUser
    {
        private IPhone _phone;
        public PhoneUser(IPhone phone)
        {
            _phone = phone;
        }

        public void UserPhone()
        {
            _phone.Dail();
            _phone.PickUp();
            _phone.Send();
            _phone.Receive();
        }
    }

    interface IPhone
    {
        void Dail();
        void PickUp();
        void Send();
        void Receive();

    }

    class NokiaPhone : IPhone
    {
        public void Dail()
        {
            Console.WriteLine("Nokia calling...");
        }

        public void PickUp()
        {
            Console.WriteLine("Hello!This is Lee!");
        }

        public void Receive()
        {
            Console.WriteLine("Nokia message ring...");
        }

        public void Send()
        {
            Console.WriteLine("Hello");
        }
    }

    class EricssonPhone : IPhone
    {
        public void Dail()
        {
            Console.WriteLine("Nokia calling...");
        }

        public void PickUp()
        {
            Console.WriteLine("Hello!This is Lee!");
        }

        public void Receive()
        {
            Console.WriteLine("Nokia message ring...");
        }

        public void Send()
        {
            Console.WriteLine("Hello");
        }
    }
}
