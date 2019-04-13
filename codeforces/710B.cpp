#include <bits/stdc++.h>

using namespace std;

int n, cute[300001]; 

int main() {
  scanf("%d\n", &n); 
  for (int i = 0; i < n; i++) {
    scanf("%d", &cute[i]);
  }
  sort(cute, cute+n);
  printf("%d", cute[(n - 1)/2]);
  return 0; 
}