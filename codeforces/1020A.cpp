#include <bits/stdc++.h>

using namespace std;

int n, h, a, b, k, ta, tb, fa, fb;

int main(){
  scanf("%d %d %d %d %d", &n, &h, &a, &b, &k);
  for (int i = 0; i < k; i++) {
    scanf("%d %d %d %d", &ta, &fa, &tb, &fb);

    int ans = 0; 
    if (ta != tb) {
      if (fa < a) {
        ans += a - fa;
        fa += a - fa;
      } else if (fa > b) {
        ans += fa - b; 
        fa -= fa - b; 
      }
    }
    ans += abs(ta - tb);
    ans += abs(fa - fb);

    cout << ans << endl;
  }
  return 0;
}
