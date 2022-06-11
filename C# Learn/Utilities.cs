using System;
namespace CSharpLearn
{
    public class Utilities<T> where T : IComparable
    {
        public T Max<T>(T a, T b)
        {
            return a.CompareTo(b) > 0 ? a : b;
        }
    }
}
