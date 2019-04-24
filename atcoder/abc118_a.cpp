#include <bits/stdc++.h>
using namespace std;

int a, b;
int main() {
  scanf("%d %d", &a, &b);
  if (!(b % a)) {
    cout << a + b;
  } else {
    cout << b - a;
  }

  return 0;
} 