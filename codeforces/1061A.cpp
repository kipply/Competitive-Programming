#include <bits/stdc++.h>

using namespace std;

int n, s;

int main(){
  scanf("%d %d", &n, &s); 


  for (int x = 1; x <= 1000000001; x++) {
    if (n * x >= s) {
      cout << x; 
      return 0;
    }
  }
  return 0;
}
