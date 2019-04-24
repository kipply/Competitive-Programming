#include <bits/stdc++.h>

using namespace std;

int n, m, a[1000006], psa[1000006];

int main(){
  scanf("%d", &n); 

  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }

  psa[0] = a[0]; 
  for (int i = 1; i < n; i++) {
    psa[i] = a[i] + psa[i - 1]; 
  }




  for (int i = 0; i < n - 1; i++) {
    cute.push_back(a[i]);
    if (gcd(a[i], a[i + 1]) != 1) {
      cute.push_back(1);
      ans++; 
    }
  }



  return 0;
}
 