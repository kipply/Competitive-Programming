#include <bits/stdc++.h>

using namespace std;

int w, h, k, ans; 
char s[101];

int main(){
  scanf("%d %d %d", &w, &h, &k);

  for (int i = 0; i < k; i++) { 
    ans += 2* w + 2 * h - 4; 
    w -= 4; 
    h -= 4; 
  }
  cout << ans;
  return 0;
}
