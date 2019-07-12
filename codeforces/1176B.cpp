#include <bits/stdc++.h>

using namespace std;

int t;

int main(){
  scanf("%d", &t); 
  for (int _ = 0; _ < t; _++) {
    int n, a[101];
    scanf("%d", &n); 
    for (int i = 0; i < n; i++) {
      scanf("%d", &a[i]); 
    }
    int ans = 0; 
    int ones = 0; 
    int twos = 0; 
    for (int i = 0; i < n; i++) {
      if (a[i] % 3 == 0) {
        ans++; 
      } else if (a[i] % 3 == 1) {
        ones++; 
      } else {
        twos++; 
      }
    }
    int t = min(ones, twos);
    ans += t; 
    ones -= t; 
    twos -= t; 
    ans += ones / 3; 
    ans += twos / 3; 
    printf("%d\n", ans);
  }
  return 0;
}

