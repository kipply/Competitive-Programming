#include <bits/stdc++.h>

using namespace std;

int t, L, v, l, r, ans; 

int main(){
  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    ans = 0;
    scanf("%d %d %d %d", &L, &v, &l, &r); 
    cout << L / v - r / v  + (l - 1) / v << endl;
  }
  return 0;
}