#include <bits/stdc++.h>

using namespace std;

char s[101];

int main(){
  scanf("%s", &s[0]);
  int last = strlen(s);
  string ans = "yes"; 
  int count = 0; 
  int first = last - 1; 
  for(int i = 0; i < last; i++) {
    if (s[i] == '1') {
      count++; 
      if (first == last - 1) first = i;
    }   
  }
  if (last - first + 1 - count < 7) ans = "no"; 
  cout << ans;
  return 0;
}
