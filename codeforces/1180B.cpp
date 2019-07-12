#include <bits/stdc++.h>

using namespace std;

int n, a[100005]; 

int main(){
  scanf("%d", &n);

  int lo = 1 << 30; 
  int loi = 0; 
  for (int i = 0; i < n; i++){ 
    scanf("%d", &a[i]); 
    if (a[i] >= 0) {
      a[i] = -a[i] - 1; 
    }
    if (a[i] < lo) {
      lo = a[i];
      loi = i; 
    }
  }

  if (n % 2) {
    a[loi] = -a[loi] - 1; 
  }

  for (int i = 0; i < n; i++) {
    printf("%d ", a[i]);
  }

  return 0;
}