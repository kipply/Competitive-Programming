#include <bits/stdc++.h>

using namespace std;

int n, k, ans; 
char s[51];

int main(){
  scanf("%d %d", &n, &k);
  scanf("%s", &s[0]);

  sort(s, s + n);
  int count = 0;
  string sub = "";
  for (int i = 0; i < n; i++) {
    if (string::npos == sub.find(s[i])) {
      bool f = true;
      for (int j = 0; j < sub.length(); j++) {
        if (abs(sub[j] - s[i]) < 2) {
          f = false;
          break;
        }
      }
      if (f) {
        sub += s[i]; 
        ans += s[i] - 96;
      }
    }
    if (sub.length() == k) break;
  }
  if (sub.length() < k) ans = -1; 
  cout << ans;
  return 0;
}