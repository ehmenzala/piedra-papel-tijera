import scala.util.Random

class GuessGame() {

  var points: Int = Integer.parseInt(History.readPointsData)

  def startGame: Unit = {
    println("--------")
    println("Bienvenido al juego de adivinanzas")
    println(">>> [A] Nueva partida")
    println(">>> [B] Récord de puntos")
    val userInput = scala.io.StdIn.readLine()
    
    if (userInput.equals("A")) {
      startGuess
    } else{
      startHistory
    }
  }
  
  def startHistory: Unit = {
    println(s"Puntos actuales: ${points}")
    println(">>> [M] Regresar al menú")
    val userChoice = scala.io.StdIn.readLine()
    if (userChoice.equals("M")) {
      startGame
    }
  }

  def startGuess: Unit = {
    println("Adivina adivinador, en qué cara de la moneda estoy pensando yo.")
    print("¿Cara o Sello? \n>>> ")
    val userGuess = scala.io.StdIn.readLine()
    testGuess(userGuess)

    println(">>> [V] Volver a jugar")
    println(">>> [M] Volver al menú")
    val userChoice = scala.io.StdIn.readLine()
    if (userChoice.equals("V")) {
      startGuess
    } else {
      startGame
    }

  }

  def testGuess(guess: String): Unit = {
    val randomFace = thinkOnFace
    if (guess.equals(randomFace)) {
      println(s"¡Ganaste! :) (+25) Estaba pensando en ${randomFace}")
      points += 25
      History.updatePointsData(points)
    } else {
      println(s"Perdiste... ): (-5) Estaba pensando en ${randomFace}")
      points -= 5
      History.updatePointsData(points)
    }
  }

  def thinkOnFace: String = {
    val options = new Array[String](2)
    options(0) = "Cara"
    options(1) = "Sello"
    val rand = new Random()
    val randomOption = rand.nextInt(2)
    val randomFace = options(randomOption)

    return randomFace
  }


}
