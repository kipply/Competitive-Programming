#include <bits/stdc++.h>

using namespace std;

int n, L, l, a, t, day[1000001], ans; 
vector< pair<int, int> > cactus; 

int main(){
  scanf("%d %d %d", &n, &L, &a);
  for (int i = 0; i < n; i++) {
    scanf("%d %d", &t, &l);
    cactus.push_back(pair<int, int>(t, l));
  }

  sort(cactus.begin(), cactus.end()); 

  int x = 0; 
  int y; 
  if (n) {
    y = cactus[0].first;
  } else {
    y = L;
  }
  for (int i = 0; i < n; i++) {
    ans += (y - x) / a; 
    if (i == n - 1) y = L;
    else y = cactus[i + 1].first;
    x = cactus[i].first + cactus[i].second; 
  }
  ans += (y - x) / a; 
  cout << ans;
  return 0;
}