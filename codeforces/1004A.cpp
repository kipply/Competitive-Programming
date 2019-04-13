#include <bits/stdc++.h>

using namespace std;

int n, d, x[101], ans; 

int main(){
  scanf("%d %d", &n, &d);
  for (int i = 0; i < n; i++) {
    scanf("%d", &x[i]);
  }

  ans = 2;

  if (x[1] - (x[0] + d) > d) ans++;
  if (x[n - 1] - d - x[n - 2] >= d) ans++;

  for (int i = 1; i < n - 1; i++) {
    if (x[i + 1] - (x[i] + d) >d) {
      ans++;
    }
    if (x[i] - d - (x[i - 1]) >= d){
      ans++;
    }

  }
  
  if (n == 1) ans = 2;
  cout << ans;
  return 0;
}
