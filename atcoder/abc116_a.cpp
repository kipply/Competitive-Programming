#include <bits/stdc++.h>
using namespace std;

int a, b, c; 
int main() {
  scanf("%d %d %d", &a, &b, &c);
  if (c > a && c > b) {
    cout << (a * b / 2);
  } else if (b > a && b > c) {
    cout << (a * c / 2); 
  } else {
    cout << (b * c / 2);
  }
  return 0;
} 