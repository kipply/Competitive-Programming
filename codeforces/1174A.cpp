#include <bits/stdc++.h>

using namespace std;

int n, a[2001];

int main(){
  scanf("%d", &n);
  for (int i = 0; i < n * 2; i++) {
    scanf("%d", &a[i]);
  }

  sort(a, a + n * 2);

  int sumL = 0; 
  int sumR = 0; 

  for (int i = 0; i < n * 2; i++) {
    if (i < n) {
      sumL += a[i]; 
    } else { 
      sumR += a[i]; 
    }
  } 

  if (sumL != sumR) {
    for (int i = 0; i < n * 2; i++) {
      printf("%d ", a[i]);
    } 
  } else {
    printf("-1");
  }
  return 0;
}
