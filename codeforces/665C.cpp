#include <bits/stdc++.h>

using namespace std;

char s[200001]; 

string alph = "abcdefghijklmnopqrstuvwxyz";

int main(){
  scanf("%s", &s[0]);
  int n = strlen(s);


  for (int i = 0; i < n; i++) {
    int start = i; 
    int end = i + 1; 
    while(end < n && s[start] == s[end]) {
      end++; 
    }
    char change;  
    if (end - start > 1){
      for (int j = 0; j < 27; j++) {
        if (alph[j] != s[start - 1] && alph[j] != s[end] &&  alph[j] != s[start]){
          change = alph[j];
          break;
        }
      }
      for (int j = start + 1; j < end; j += 2) {
        s[j] = change; 
      }
    }
    i = end - 1; 
  }

  cout << s; 
  return 0;
}
