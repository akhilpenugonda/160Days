using System;

namespace CSharpLearn
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            var numbers = new GenericList<int>();
            numbers.Add(10);
            var books = new GenericList<string>();
            books.Add("hello");

            var dictionary = new GenericDictionary<string, int>();
            dictionary.Add("1234", 12);
        }
    }

    public class GenericDictionary<TKey, TValue>
    {
        public void Add(TKey key, TValue value)
        {

        }
    }
    public class GenericList<T>
    {
        public void Add(T value)
        {

        }
        public T this[int value]
        {
            get { throw new NotImplementedException(); }
        }

    }
}
