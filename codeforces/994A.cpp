#include <bits/stdc++.h>

using namespace std;

int n, m, x[11], y[11], keys[10];

int main(){
  scanf("%d %d", &n, &m); 
  for (int i = 0; i < n; i++) {
    scanf("%d", &x[i]);
  }
  for (int i = 0; i < m; i++) {
    scanf("%d", &y[i]);
    keys[y[i]] = 1; 
  }

  for (int i = 0; i < n; i++) {
    if (keys[x[i]]) {
      cout << x[i]; 
      cout << " ";
    }
  }
  return 0;
}
