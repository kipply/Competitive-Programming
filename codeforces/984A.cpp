
#include <bits/stdc++.h>

using namespace std;

int n, a[1001]; 

int main(){
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }
  sort(a, a + n); 

  cout << a[(n - 1) / 2];
}
