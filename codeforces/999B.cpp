#include <bits/stdc++.h>

using namespace std;

int n; 
string s; 

int main(){
  scanf("%d\n", &n);
  getline(cin, s);

  for (int i = 1; i < n + 1; i++) {
    if (!(n % i)) {
      reverse(s.begin(), s.begin() + i);
    }
  }
  cout << s;
  return 0;
}