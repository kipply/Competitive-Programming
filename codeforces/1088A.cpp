
#include <bits/stdc++.h>

using namespace std;

int n; 

int main(){
  scanf("%d", &n);
  for (int a = 1; a <= n; a++) {
    for (int b = a; b <= n; b += a) {
      if (a * b > n && b / a < n) {
        printf("%d %d", b, a);
        return 0;
      }
    }
  }
  cout << -1; 
  return 0;
}
