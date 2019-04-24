#include <bits/stdc++.h>
using namespace std;

int k; 
int main() { 
  scanf("%d", &k);
  int odds = k / 2; 
  int evens = k / 2; 
  if (k % 2) {
    odds++; 
  } 
  cout << odds * evens;
  return 0;
} 