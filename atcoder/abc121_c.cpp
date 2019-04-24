#include <bits/stdc++.h>
using namespace std;

long long int n, m, a, b; 
vector< pair<int, int> > stores; 
long long int ans;

int main() { 
  scanf("%lld %lld", &n, &m);
  for (int i = 0; i < n; i++) {
    scanf("%lld %lld", &a, &b);
    stores.push_back(make_pair(a, b));
  }
  sort(stores.begin(), stores.end());
  for (auto store : stores) {
    if (m == 0) break;
    if (store.second >= m) {
      ans += store.first * m; 
      m = 0;
    } else {
      m -= store.second; 
      ans += store.first * store.second;
    }
  }

  printf("%lld\n", ans);
  return 0;
} 