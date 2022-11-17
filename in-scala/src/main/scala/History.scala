import java.io.{File, FileWriter, PrintWriter}
import java.nio.file.ProviderNotFoundException
import java.util.Scanner

object History {

  def readPointsData: String = {
    var currentPoints: String = ""
    val myFile = new File("./points.txt")
    val sc = new Scanner(myFile)

    while (sc.hasNextLine()) {
      currentPoints = sc.nextLine()
    }

    sc.close()

    return currentPoints

  }

  def updatePointsData(newPoints: Int): Unit = {
    var fw = new FileWriter("./points.txt")
    var pw = new PrintWriter(fw)

    pw.println(newPoints)
    pw.close()
  }
}
