#include <bits/stdc++.h>
#include <stdio.h>

using namespace std;
int main(){
  int a[3];

  scanf("%d %d %d", &a[0], &a[1], &a[2]);
  sort(a, a + 3);
  cout << a[1];
  return 0;
}
