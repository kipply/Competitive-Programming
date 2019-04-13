#include <bits/stdc++.h>

using namespace std;

int n, x, y; 
int ans; 

int main(){
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d %d", &x, &y);
    ans = max(ans, x + y);
  }
  cout << ans;
  return 0;
}