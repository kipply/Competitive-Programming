// Worse code cannot be found. 

import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int n = s.nextInt();
    String looo = s.nextLine();
    for(int l = 0; l < n; l++){
      String boop = s.nextLine();
      String y = boop.split(" ")[1];
      String x = boop.split(" ")[0];
      Boolean negative = false;
      Boolean subtract = false;
      Boolean twoNegativeZeros = false;
      if (x.equals("-0") && y.equals("-0")){
        twoNegativeZeros = true;
      }
      String temp;
      if(x.charAt(0) == '-' && y.charAt(0) == '-'){
        negative = true;
        x = x.substring(1);
        y = y.substring(1);
      } else if(x.charAt(0) == '-'){
        subtract = true;
        x = x.substring(1);
        temp = x;
        x = y;
        y = temp;
      } else if(y.charAt(0) == '-'){
        subtract = true;
        y = y.substring(1);
      }
      if(subtract){
        if (y.length() > x.length()){
          negative = true;
          temp = x;
          x = y;
          y = temp;
        }
        else if(y.length() == x.length()){
          for (int i = 0; i < y.length(); i++){
            if (Character.getNumericValue(y.charAt(i)) > Character.getNumericValue(x.charAt(i))){
                        negative = true;
                        temp = x;
                        x = y;
                        y = temp;
                        break;
            }
            else if (Character.getNumericValue(y.charAt(i)) < Character.getNumericValue(x.charAt(i))){
                        break;
            }
          }
        }
      }
      int zeros;
      if(x.length() > y.length()){
        zeros = x.length() - y.length();
        for(int i = 0; i < zeros; i++){
          y = "0" + y ;
        }
      } else if(x.length() < y.length()){
        zeros = y.length() - x.length();
        for(int i = 0; i < zeros; i++){
          x = "0" + x;
        }
      }
      String[] ta = new String[x.length()];
      String[] tb = new String[y.length()];

      if(x.charAt(0) == '-' && y.charAt(0) == '-'){
        ta = x.substring(1).split("");
        tb = y.substring(1).split("");
        negative = true;
      } else if(x.charAt(0) == '-'){
        tb = x.substring(1).split("");
        ta = y.split(" ");
        subtract = true;
      } else if (y.charAt(0) == '-'){
        ta = x.split(" ");
        tb = y.substring(1).split("");
        subtract = true;
      } else{
        ta = x.split("");
        tb = y.split("");
      }
      int[] a = new int[ta.length];
      int[] b = new int[tb.length];
      for(int i = 0; i < ta.length; i++){
        a[i] = Integer.parseInt(ta[i]);
      }
      for(int i = 0; i < tb.length; i++){
        b[i] = Integer.parseInt(tb[i]);
      }

      int longer = a.length;

      int carry = 0;
      int[] ans = new int[longer + 1];

      int aa, bb;
      if(subtract){ //Array lengths match, (used preceding zeros). a > b and no negative signs
        for(int i = 0; i < longer; i++){ //longer is just the length
          aa = a.length - 1 - i; // So we can count from the end of the array
          bb = b.length - 1- i; // Idk why I used two variables, it just felt right. I know they'll always be equal
          if (a[aa] - b[bb] - carry < 0){
            ans[longer - i] = (a[aa] + 10 - b[bb] - carry);
            carry = 1;
          } else{
            ans[longer - i] = a[aa] - b[bb] - carry;
            carry = 0;
          }
        }
      } else{
        for(int i = 0; i < longer; i++){
          aa = a.length - 1 - i;
          bb = b.length - 1- i;
          if (a[aa] + b[bb] + carry > 9){
            ans[longer - i] = (a[aa] + b[bb] + carry) - 10;

            carry = 1;
          } else{
            ans[longer - i] = a[aa] + b[bb] + carry;
            carry = 0;
          }
          if (i + 1 == longer && carry == 1){
            ans[longer - i - 1] = 1;
          }
        }
      }
      if(negative){
        if (!twoNegativeZeros){
        System.out.print("-");
        }
      }
      Boolean zero = false;
      for (int i = 0; i < ans.length; i++){
        if (!zero && ans[i] == 0){

        } else{
        System.out.print(ans[i]);
        zero = true;
        }
      }
      if(!zero){
        System.out.print("0");
      }
      if(l + 1 != n){
      System.out.println("");
      }
    }
  }
}
