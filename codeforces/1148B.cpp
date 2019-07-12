
#include <bits/stdc++.h>

using namespace std;

int n, m, ta, tb, k, a[200001], b[200001]; 


int main(){
  scanf("%d %d %d %d %d", &n, &m, &ta, &tb, &k); 

  for (int i = 0; i < n; i++) { 
    scanf("%d", &a[i]); 
  }

  for (int i = 0; i < m; i++) {
    scanf("%d", &b[i]); 
  }


  if (k >= n || k >= m) {
    printf("-1"); return 0; 
  }

  int best = -1; 
  for (int i = 0; i <= k; i++) {
    int x = 0; 

    int lo = 0; 
    int hi = m; 
    while (lo <= hi) {
      int g = (lo + hi) / 2; 
      if (b[g] >= a[i] + ta) {
        x = g; 
        hi = g - 1; 
      } else {
        lo = g + 1; 
      }
    }
    x++; 

    if (x + k - i > m || a[i] + ta > b[m - 1]) {
      best = -1; 
      break; 
    }
    best = max(best, b[x + k - i - 1] + tb);
  }

  printf("%d\n", best); 
  return 0;
}