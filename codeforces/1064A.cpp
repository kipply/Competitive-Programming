#include <bits/stdc++.h>

using namespace std;

int a, b, c;

int main(){
  scanf("%d %d %d", &a, &b, &c);
  for (int i = 0; i < 101; i++) {
    if (a + b > c && a + c > b && b + c > a) {
      cout << i; 
      return 0; 
    } else {
      int lo = min(min(a, b), c); 
      if (lo == a) a++; 
      else if (lo == b) b++; 
      else if (lo == c) c++;
    }
  }
  return 0;
}
