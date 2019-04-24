
#include <bits/stdc++.h>

using namespace std;

int n, m, d[1000010], a[1000010]; 
int examlocs[1000010]; 
int examorder[1000010]; 

int main(){
  scanf("%d %d", &n, &m); 
  for (int i = 0; i < n; i++) {
    scanf("%d", &d[i]); 
  }

  for (int i = 0; i < m ; i++) {
    scanf ("%d", &a[i]); 
  }

  int lo = 0; 
  int hi = n + 1; 
  int ans = -1; 

  while (lo <= hi) {
    memset(examorder, 0, 1000010); 
    memset(examlocs, 0, 1000010); 
    // printf("%d %d\n", lo, hi);

    int cnt = 0; 
    int mid = (lo + hi + 1) / 2; 
    for (int i = mid; i >= 0; i--) {
      if (examlocs[d[i]] == 0 && d[i] != 0) {
        examlocs[d[i]] = i;
        examorder[m - cnt - 1] = d[i]; 
        cnt++; 
      }
      if (cnt > m) {
        break; 
      }
    }
    long long int used = 0; 
    bool possible = true;
    for (int i = 0; i < m; i++) {
      if ((examlocs[examorder[i]] - used) - i >= a[examorder[i] - 1]) {
        used += a[examorder[i] - 1]; 
      } else {
        possible = false;
      }
    }
    if (cnt != m) { 
      possible = false;
    }

    if (possible) {
      hi = mid - 1; 
      if (ans == -1) {
        ans = mid; 
      }
      ans = min(mid, ans);
    } else {
      lo = mid + 1; 
    }
  }
  if (ans != -1) { ans++; }
  cout << ans << endl; 
  return 0;
}
