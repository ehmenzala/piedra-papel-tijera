namespace in_csharp
{
    internal class Program
    {
        static int points = int.Parse(File.ReadAllText("points.txt"));

        static void Main(string[] args)
        {
            startGame();
        }

        public static void writePoints(int currentPoints)
        {
            String currentStringPoints = currentPoints.ToString();
            File.WriteAllText("points.txt", currentStringPoints);
        }

        public static void startGame()
        {
            Console.WriteLine("-------");
            Console.WriteLine("¡Bienvenido!");
            Console.WriteLine(">>> Iniciar [A]");
            Console.WriteLine(">>> Puntos [B]");
            String userInput = Console.ReadLine();

            if (userInput == "A")
            {
                startGuess();
            }
            else
            {
                Console.WriteLine(points);
                Console.WriteLine(">>> ¿Regresar al menu? [M]");
                String userMenu = Console.ReadLine();
                if (userMenu == "M")
                {
                    startGame();
                }

            }

        }

        public static void startGuess()
        {
            Console.WriteLine("Adivina, adivinador. En qué cara del dado estoy pensando yo.");
            int randomFace = thinkOnFace();
            int userAnswer = int.Parse(Console.ReadLine());

            if (randomFace == userAnswer)
            {
                Console.WriteLine($"Ganase 10 puntos, estaba pensando en {randomFace}");
                points += 10;
            }
            else
            {
                Console.WriteLine($"Perdiste 2 puntos, estaba pensando en {randomFace}");
                points -= 2;
            }

            writePoints(points);

            Console.WriteLine("¿Quieres volver a jugar? (Y/N)");
            String userInput = Console.ReadLine();
            if (userInput == "Y")
            {
                startGame();
            }
        }

        public static int thinkOnFace()
        {
            int[] faces = { 1, 2, 3, 4, 5, 6 };
            Random rnd = new Random();
            int randomIndex = rnd.Next(faces.Length);
            int randomFace = faces[randomIndex];

            return randomFace;
        }
    }
}
