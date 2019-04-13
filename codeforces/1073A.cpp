
#include <bits/stdc++.h>

using namespace std;

int n; 
char s[1001]; 
map<char, int> cute; 
int main(){
  scanf("%d\n%s", &n, &s[0]);
  for (int i = 0; i < n - 1; i++) { 
    if (s[i] != s[i + 1]) {
      printf("YES\n");
      cout << s[i]; 
      cout << s[i + 1];
      return 0;
    }
  }
  printf("NO");
  return 0;
}
