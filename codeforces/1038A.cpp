#include <bits/stdc++.h>

using namespace std;

int n, k;
string s;
char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
int ans = 1 << 30; 

int main(){
  scanf("%d %d\n", &n, &k);
  getline(cin, s);

  for (int i = 0; i < k; i++) {
    ans = min((int)count(s.begin(), s.end(), alphabet[i]), ans);
  }

  cout << ans * k;
  return 0;
}

