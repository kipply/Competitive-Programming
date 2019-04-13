#include <bits/stdc++.h>

using namespace std;

char s[101];
int cute; 

int main(){
  scanf("%s", &s[0]);
  for (int i = 0; i < strlen(s); i++) {
    if (s[i] == '-') cute++;
  }
  if (cute == 0 || cute == strlen(s) || cute % (strlen(s) - cute) == 0 ) {
    cout << "YES"; 
  } else {
    cout << "NO";
  }
  return 0;
}