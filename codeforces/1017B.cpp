#include <bits/stdc++.h>
#include <stdio.h>

using namespace std;

long long int n, zeros, ones, x, y;
char a[200001], b[200001];

int main(){
  scanf("%llu\n", &n); 
  for (int i = 0; i < n; i++) {
    scanf("%c", &a[i]);
  }
  scanf("\n");
  for (int i = 0; i < n; i++) {
    scanf("%c", &b[i]);
  }

  for (int i = 0; i < n; i++) {
    if (a[i] == '1') {
      ones++;
    } else {
      zeros++;
    }

    if (b[i] == '0') {
      if (a[i] == '1') {
        y++;
      } else {
        x++;
      }
    }
  }
  cout << x * ones + y * zeros - x * y;

  return 0;
}
