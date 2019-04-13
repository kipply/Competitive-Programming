#include <bits/stdc++.h>

using namespace std;

int n, l, r, m, chess_lo, chess_hi, programming_lo, programming_hi;

int main(){
  chess_lo = 1 << 30; 
  programming_lo = 1 << 30; 

  scanf("%d", &n); 
  for (int i = 0; i < n; i++) {
    scanf("%d %d", &l, &r); 
    chess_hi = max(l, chess_hi); 
    chess_lo = min(r, chess_lo);
  }
  scanf("%d", &m); 
  for (int i = 0; i < m; i++) {
    scanf("%d %d", &l, &r); 
    programming_hi = max(l, programming_hi); 
    programming_lo = min(r, programming_lo);
  }

  cout << max(max(programming_hi - chess_lo, chess_hi - programming_lo), 0);


  return 0;
}
