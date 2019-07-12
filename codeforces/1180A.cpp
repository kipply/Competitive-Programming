#include <bits/stdc++.h>

using namespace std;

int n; 

int main(){
  scanf("%d", &n);
  int ans = 1; 
  int c = 4; 
  for (int i = 0; i < n - 1; i++) {
    ans += c; 
    c += 4; 
  } 
  printf("%d", ans); 
  return 0;
}