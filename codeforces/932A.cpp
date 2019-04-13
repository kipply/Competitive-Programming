#include <bits/stdc++.h>

using namespace std;

char a[1001];

int main(){
  scanf("%s", &a[0]);
  int n = strlen(a);
  cout << a; 
  for (int i = 0; i < n; i++) {
    cout << a[n - i - 1];
  }
  return 0;
}
