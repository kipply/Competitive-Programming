#include <bits/stdc++.h>

using namespace std;

int n, a[100001], ans; 
map<int, int> cute; 

int main(){
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
    cute[a[i]] += 1;
  }

  for (auto const& x : cute) {
    ans = max(ans, x.second);
  }
  cout << n - ans;
  return 0;
}