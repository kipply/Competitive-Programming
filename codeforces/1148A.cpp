#include <bits/stdc++.h>

using namespace std;

long long int a, b, c; 
long long int ans; 

int main(){
  scanf("%lld %lld %lld", &a, &b, &c);


  ans += 2 * min(a, b); 
  if (b != 0) {
    ans += 2 * c; 
  }

  if (a > b) {
    ans += 1; 
  }

  if (b > a) {
    ans += 1;
  }

  cout << ans; 
  return 0;
}