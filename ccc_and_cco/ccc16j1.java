import java.util.*;
public class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int w = 0;
    String in;
    for (int i = 0; i < 6; i++){
      in = s.nextLine();
      if (in.equals("W")){
        w++;
      }
    }
    int ans = 0;
    if (w == 5 || w == 6){
      ans = 1;
    }
    if (w == 4 || w == 3){
      ans = 2;
    }
    if (w == 0){
      ans = -1;
    }
    if (w == 1 || w == 2){
      ans = 3 ;
    }
    System.out.println(ans);
  }
}
