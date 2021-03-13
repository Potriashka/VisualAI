Random rnd = new Random ();
byte number = rnd.Next(0, 10);
Console.WriteLine("угадай число за 3 попытки");
byte n = 0;
While(n < 3) { 
    byte answer = int.Parse(Console.ReadLine("ваше число:"));
    if (answer == number) }
    Console.WriteLine($ "угадал с {n} попыток");
    } else {
    Console.WriteLine("не угадал, осталось:" + (3-n) toString() + "попыток"); n++; }
    }
