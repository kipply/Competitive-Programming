#include <bits/stdc++.h>
using namespace std;


char s[3];

int main() { 
  scanf("%s", &s[0]);
  for (int i = 0; i < strlen(s); i++) {
    if (s[i] == '9') {
      cout << '1';
    } else {
      cout << '9';
    }
  }
  return 0;
} 