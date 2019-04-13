#include <bits/stdc++.h>

using namespace std;

char s[100]; 

int main(){
  scanf("%s", &s[0]);
  int n = strlen(s);
  int count = 0;
  for (int i = 0; i < n / 2; i++) {
    if (s[i] != s[n - 1 - i]) {
      count++; 
    }
  }
  if (count == 1 || (n % 2 && count == 0)) {
    cout << "YES"; 
    return 0; 
  }
  cout << "NO";
  return 0;
}