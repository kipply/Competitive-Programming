import java.util.*;
public class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int[][] square = new int[4][4];
    for (int i = 0; i < 4; i++){
      for (int j = 0; j < 4; j++){
        square[i][j] = s.nextInt();
      }
    }
    int test = 0;

    for (int i = 0; i < 1; i++){
      for (int j = 0; j < 4; j++){
        test += square[i][j];
      }
    }
    int boop = 0;
    boolean flag = true;
    for (int i = 1; i < 4; i++){
      for (int j = 0; j < 4; j++){
        boop += square[i][j];
      }
      if (boop != test){
        flag = false;
      }
      boop = 0;
    }
    for (int i = 0; i < 4; i++){
      for (int j = 0; j < 4; j++){
        boop += square[j][i];
      }
      if (boop != test){
        flag = false;
      }
      boop = 0;
    }
    if (flag){
      System.out.println("magic");
    } else{
      System.out.println("not magic");
    }
  }
}
