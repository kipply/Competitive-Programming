#include <bits/stdc++.h>

using namespace std;

int n; 
char s[101];

int main(){
  scanf("%d", &n);
  scanf("%s", &s[0]);

  int ones = 0; 
  for (int i = 0; i < n; i++) {
    if (s[i] == '1') ones++;
  }

  if (ones) cout << '1';
  for (int i = 0; i < n - ones ; i++) cout << '0';
  return 0;
}
