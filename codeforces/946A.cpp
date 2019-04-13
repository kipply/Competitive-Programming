#include <bits/stdc++.h>

using namespace std;

int n, a[101], pos, neg; 

int main(){
  scanf("%d\n", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
    if (a[i] > 0) {
      pos += a[i]; 
    } else {
      neg -=a[i]; 
    }
  }

  cout << pos + neg;
  return 0;
}