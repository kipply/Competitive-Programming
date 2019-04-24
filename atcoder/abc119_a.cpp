#include <bits/stdc++.h>
using namespace std;


int y, m, d;

int main() {
  scanf("%d/%d/%d", &y, &m, &d);
  if (m < 4 || (m == 4 && d <= 30)) {
    cout << "Heisei";
  } else {
    cout << "TBD";
  }
  return 0;
} 