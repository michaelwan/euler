import java.time.Instant;

//find the sum of all numbers less than 1000 that are either multiply of 3 or 5
public class Problem1 {
  public static void main(String[] args) {
    Instant begin = Instant.now();
    basicMethod();
    Instant end = Instant.now();
    System.out.println("Basic method consumed second " + (end.getEpochSecond()-begin.getEpochSecond()));
    System.out.println("Basic method consumed nano second " + (end.getNano()-begin.getNano()));
  }

  private static void basicMethod () {
    long sum = 0;
    for (int i = 1; i<100000; i++) {
      if((i%3 == 0) || (i%5 == 0)) {
        System.out.print(i + " ");
        sum = sum + i;
      }
    }
    System.out.println("\nTotal is " + sum);
  }

}
