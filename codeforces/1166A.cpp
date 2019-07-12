#include <bits/stdc++.h>

using namespace std;

int n; 
int people[150]; 
char s[100]; 

int nc2(int n) {
  return n * (n - 1) / 2; 
}
int main(){
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%s", &s[0]);
    people[s[0]]++;
  }

  long long int ans = 0; 
  for (int i = 97; i < 123; i++) {
    int n = (people[i] + 1) / 2;
    ans += nc2(people[i] / 2); 
    ans += nc2((people[i] + 1) / 2); 
  }

  cout << ans;
  return 0;
}