#include <bits/stdc++.h>

using namespace std;

char s[200001];

int main(){
  int cute; 
  scanf("%d", &cute);
  scanf("%s", &s[0]);
  int n = strlen(s);

  int idx = 0; 

  for (int i = 0; i < n; i++) {
    idx = i; 
    if (s[i] > s[i + 1]) {
      break;
    }
  }

  for (int i = 0; i < n; i++) {
    if (i != idx) {
      cout << s[i];
    }
  }
  return 0;
}
