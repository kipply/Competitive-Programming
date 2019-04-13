#include <bits/stdc++.h>

using namespace std;

char s[101];

int main(){
  scanf("%s", &s[0]);
  if (strstr(s, "ABC") || strstr(s, "ACB") || strstr(s, "BAC") || strstr(s, "BCA") || strstr(s, "CAB") || strstr(s, "CBA")) {
    cout << "Yes";
    return 0;
  } else {
    cout << "No";
  }
}
