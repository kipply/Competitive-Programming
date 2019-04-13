#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> ans; 

int main(){
  scanf("%d", &n);

  for (int i = max(1, n - 100); i < n; i++) {
    int sum = i;
    int x = i; 
    while (x > 0) {
      sum += x % 10; 
      x /= 10;
    }
    if (sum == n) {
      ans.push_back(i);
    }
  }

  cout << ans.size() << endl; 
  for (auto &i : ans) { 
    cout << i << endl;
  }
  return 0;
}

