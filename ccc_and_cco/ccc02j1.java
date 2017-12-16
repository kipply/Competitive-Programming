import java.util.*;
public class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int
    n = s.nextInt();
    if (n == 9){
      System.out.println(" * * *\n*     *\n*     *\n*     *\n * * *\n      *\n      *\n      *\n * * *");

    } else if (n == 8){
      System.out.println(" * * *\n*     *\n*     *\n*     *\n * * *\n*     *\n*     *\n*     *\n * * *");

    } else if (n == 7){
            System.out.println(" * * *\n      *\n      *\n      *\n      \n      *\n      *\n      *\n      ");
    } else if (n == 6){
            System.out.println(" * * *\n*      \n*      \n*      \n * * *\n*     *\n*     *\n*     *\n * * *");
    } else if (n == 5){
            System.out.println(" * * *\n*      \n*      \n*      \n * * *\n      *\n      *\n      *\n * * *");
    } else if (n == 4){
      System.out.println("*     *\n*     *\n*     *\n * * *\n      *\n      *\n      *");
    } else if (n == 3){
            System.out.println(" * * *\n      *\n      *\n      *\n * * *\n      *\n      *\n      *\n * * *");

    } else if (n == 2){
      System.out.println(" * * *\n      *\n      *\n      *\n * * *\n*      \n*      \n*      \n * * *");
    } else if (n == 1){
      System.out.println("      *\n      *\n      *\n      *\n      *\n      *");

    } else if (n == 0){
      System.out.println(" * * *\n*     *\n*     *\n*     *\n\n*     *\n*     *\n*     *\n * * *");

    }
  }
}
