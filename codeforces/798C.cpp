#include <bits/stdc++.h>

using namespace std;

int n, a[100001]; 

int f(int a, int b){ 
  if (a == 0) 
    return b; 
  return f(b%a, a); 
} 

int main(){
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]); 
  }

  int count = 0; 
  int ans = 0; 
  int gcd = a[0]; 
  for (int i = 0; i < n; i++) {
    gcd = f(gcd, a[i + 1]);
    if (a[i] % 2) {
      count++; 
    } else {
      ans += count / 2; 
      if (count % 2) {
        ans += 2; 
      }
      count = 0; 
    }
  }
  if (count) {
    ans += count / 2; 
    if (count % 2) {
      ans += 2; 
    }
  }

  if (gcd != 1) {
    ans = 0; 
  }

  cout << "YES" << endl; 
  cout << ans << endl;

  return 0;
}