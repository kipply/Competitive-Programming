#include <bits/stdc++.h>

using namespace std;

int n, a[200001]; 

int main(){
  scanf("%d", &n);
  int curr = 1; 
  for (int i = 2; i <= n; i++) {
    if (a[i] == 0) {
      for (int x = i; x <= n; x += i) {
        a[x] = curr; 
      }
      curr++; 
    }
  }

  for (int i = 2; i <= n; i++) {
    printf("%d ", a[i]);
  }
  return 0;
}
