#include <bits/stdc++.h>

using namespace std;

int n, a[1000001], b[1000001]; 


int main(){
  scanf("%d", &n); 
  int og_n = n;
  for (int i = 0; i < n; i++) {
    a[i] = i + 1; 

  }

  int curr = n; 
  int val = 1; 
  while (curr > 0) {
    int odds = (curr + 1) / 2; 
    if (curr == 1) {
      printf("%d ", val * 1); 
      break; 
    } else if (curr == 2) {
      printf("%d %d ", val, val * 2); 
      break; 
    } else if (curr == 3) {
      printf("%d %d %d ", val, val, val * 3); 
      break; 
    } else {
      for (int i = 0; i < odds; i++) {
        printf("%d ", val); 
      }
      val *= 2;
    }
    curr -= odds; 
  }
  return 0;
}
