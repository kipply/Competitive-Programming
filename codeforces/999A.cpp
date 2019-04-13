#include <bits/stdc++.h>

using namespace std;

int n, k, a[101], ans; 

int main(){
  scanf("%d %d", &n, &k);

  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }
  ans = 0;
  int l = 0; 
  int r = n - 1; 
  while (true) { 
    if (l > r) break;
    if (a[l] <= k) {
      l++; 
      ans++;
    } else if (a[r] <= k) {
      r--; 
      ans++; 
    } else {
      break;
    }
  }
  cout << ans;
  return 0;
}