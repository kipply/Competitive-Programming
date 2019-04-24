#include <bits/stdc++.h>
using namespace std;

int n, m, c; 
int b[21], a[21][21], ans;

int main() { 
  scanf("%d %d %d", &n, &m, &c);
  for (int i = 0; i < m; i++) {
    scanf("%d ", &b[i]);
  }  
  for (int i = 0; i < n; i++) {
    int curr = 0; 
    for (int j = 0; j < m; j++) {
      scanf("%d", &a[i][j]);
      curr += a[i][j] * b[j]; 
    }
    if (curr + c > 0) ans++;
  }

  cout << ans;

  return 0;
} 