
#include <bits/stdc++.h>

using namespace std;

int t; 

int main(){
  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    char s[1001]; 
    scanf("%s", &s[0]); 

    char cute = s[0]; 
    string ans = "-1"; 
    if (cute == s[strlen(s) - 1]) {
      for (int j = 1; j < strlen(s); j++) {
        if (s[j] != cute) {
          s[0] = s[j]; 
          s[j] = cute; 
          ans = s; 
          break; 
        }
      }
    } else {
      ans = s; 
    }
    cout << ans << endl;
  }

  return 0;
}
