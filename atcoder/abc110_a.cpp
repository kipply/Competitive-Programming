#include <bits/stdc++.h>
using namespace std;


int a, b, c; 

int main() { 
  scanf("%d %d %d", &a, &b, &c);
  if (b > a && b > c) {
    b *= 10; 
  } else if (c > b && c > a) {
    c *= 10; 
  } else {
    a *= 10; 
  } 
  cout << a + b + c;
  return 0;
} 