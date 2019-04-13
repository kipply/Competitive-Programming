#include <bits/stdc++.h>

using namespace std;

int n, a[200001], b[200001];
int p, moved[200001], ans; 
int main(){
  scanf("%d", &n); 
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }
  for (int i = 0; i < n; i++) {
    scanf("%d", &b[i]);
  }

  ans = 1;
  for (int i = 0; i < n; i++) {
    if(!moved[b[i]]) {
      while (a[p] != b[i]) {
        moved[a[p]] = 1;
        p++; 
        ans++; 
      }
    }
    cout << ans; 
    cout << " ";
    ans = 0; 
  }


  return 0;
}