#include <bits/stdc++.h>

using namespace std;

int n, a[1001]; 

int main(){
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }
  int max = *max_element(a, a + n);
  int min = *min_element(a, a + n); 
  cout << abs(max - min) + 1 - n;
  return 0;
}