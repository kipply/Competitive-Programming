#include <bits/stdc++.h>

using namespace std;

char ans[10001];
char vowels[] = "aoeui";
int n; 
int main(){
  scanf("%d", &n);

  bool f = false;
  int r, c; 
  for (int i = 5; i < 10; i++) { 
    if ((n / i) * i == n && n / i >= 5) {
      r = i; 
      c = n / i;
      f = true; 
    } 
  }

  if (!f) {
    cout << -1; 
    return 0; 
  } 

  int startIdx = 0; 
  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      ans[c * i + j] = vowels[(startIdx + j) % 5];
    }
    startIdx++;
  }

  cout << ans;
  return 0;
}