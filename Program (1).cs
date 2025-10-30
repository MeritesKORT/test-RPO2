using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp6
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Введите сумму в рублях : ");
            int number = int.Parse(Console.ReadLine());
            Console.WriteLine("Введите во что перевести 1 - $ 2 - € 3 - ¥ : ");
            int answer = int.Parse(Console.ReadLine());


            switch (answer)
            {
                case 1:
                    Console.WriteLine($"{number / 80.70}$");


                    break;

                case 2:
                    Console.WriteLine($"{number  / 94.67}€");



                    break;

                case 3:
                    Console.WriteLine($"{number / 11.47}¥");



                    break;



            }
        }
    }
}
