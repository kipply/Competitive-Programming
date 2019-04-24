#include <bits/stdc++.h>

using namespace std;

int n, x, y; 
vector<int> cactus[200005];

int ans[200005], v[2000005];


int dfs(int node, int parent, int parentColour) {

  int curr = 1; 
  for (int &child : cactus[node]) {
    if (child == parent) {
      continue; 
    }
    while (curr == parentColour ||  curr == ans[node]) {
      curr++; 
    }
    if (!v[child]) {
      ans[child] = curr; 
      dfs(child, node, ans[node]); 
    }
    curr++; 
  }
  return 0; 
}

int main(){
  scanf("%d", &n); 

  for (int i = 0; i < n - 1; i++) {
    scanf("%d %d", &x, &y);
    cactus[x].push_back(y); 
    cactus[y].push_back(x);
  }

  ans[1] = 1; 
  dfs(1, 0, 0);

  cout << *max_element(ans, ans + n + 1) << endl; 
  for (int i = 1; i <= n; i++) {
    printf("%d ", ans[i]); 
  }
  return 0;
}
 