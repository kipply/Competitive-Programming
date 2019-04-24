#include <bits/stdc++.h>
using namespace std;

int n, i;
int main() { 
  scanf("%d %d", &n, &i);
  int odds = k / 2; 
  int evens = k / 2; 
  if (k % 2) {
    odds++; 
  } 
  cout << odds * evens;
  return 0;
} 