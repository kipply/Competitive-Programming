#include <bits/stdc++.h>

using namespace std;

int r, c, n, k, x, y, ans; 
bool cactus[11][11]; 

int main(){
  scanf("%d %d %d %d", &r, &c, &n, &k); 
  for (int i = 0; i < n; i++) {
    scanf("%d %d", &x, &y); 
    cactus[x - 1][y - 1] = true;
  }

  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      for (int ii = i; ii < r; ii++) {
        for (int jj = j; jj < c; jj++) {
          int count = 0; 
          for (x = i; x <= ii; x++) {
            for (y = j; y <= jj; y++) {
              if (cactus[x][y]) {
                count++; 
              }
            }
          }
          if (count >= k) {
            ans++; 
          }
        }
      }
    }
  }

  cout << ans;
  return 0;
}
