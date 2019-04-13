#include <bits/stdc++.h>

using namespace std;

long long int n, k, ans; 

int main(){
  scanf("%llu %llu", &n, &k);

  if (k - 1 < n) {
    ans += k - 1;
  } else {
    ans += n + 1; 
  }
  if (k - n > 0) {
    ans -= k - n;
    if (ans < 0) ans = 0;
  }

  cout << ans / 2;
  return 0;
}
