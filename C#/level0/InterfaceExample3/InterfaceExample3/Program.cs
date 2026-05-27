using System.Collections;

namespace InterfaceExample3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] nums1 = { 1, 2, 3, 4, 5 };
            ArrayList nums2 = new ArrayList{ 1, 2, 3, 4, 5 };
            var roc = new ReadOnlyCollection(nums1);
            foreach (int n in roc)
            {
                Console.WriteLine(n);
            }

        }

        static int Sum(ICollection nums)
        {
            int sum = 0;
            foreach (var n in nums)
            {
                sum += (int)n;
            }
            return sum;
        }
    }

    class ReadOnlyCollection : IEnumerable
    {
        private int[] _array;
        public ReadOnlyCollection(int[] array)
        {
            _array = array;
        }

        public IEnumerator GetEnumerator()
        {
            return new Enumerator(this);
        }

        public class Enumerator : IEnumerator
        {
            private ReadOnlyCollection _collection;
            private int _head;

            public Enumerator(ReadOnlyCollection collection)
            {
                _collection = collection;
                _head = -1;
            }

            public object Current
            {
                get
                {
                    object o = _collection._array[_head];
                    return o;
                }
            }

            public bool MoveNext()
            {
                if (++_head < _collection._array.Length)
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }

            public void Reset()
            {
                _head = -1;
            }
        }
    }
}
