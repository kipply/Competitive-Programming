#include <bits/stdc++.h>

using namespace std;

int n, m, a[200001], written;

int main(){
  scanf("%d %d", &n, &m);
  for (int i = 0; i < n; i++) { 
    scanf("%d", &a[i]);
    written += a[i]; 
    printf("%d ", written / m ); 
    written %= m;
  }
  return 0;
}

