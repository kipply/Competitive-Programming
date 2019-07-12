#include <bits/stdc++.h>

using namespace std;

long long int n, x; 

int main(){
  scanf("%lld", &n);
  for (int i = 0; i < n; i++) { 
    scanf("%lld", &x);
    int ans = 0; 
    while (x != 1) {

      if (x % 2 == 0) {
        x /= 2; 
      } else if (x % 3 == 0) {
        x *= 2; 
        x /= 3; 
      } else if (x % 5 == 0) {
        x *= 4; 
        x /= 5; 

      } else {
        ans = -1; 
        break; 
      }
      ans++;
    }
    cout << ans << endl; 
  }
  return 0;
}

