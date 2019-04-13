#include <bits/stdc++.h>

using namespace std;

string n1, n2, first, second; 
int n; 

int main(){
  cin >> n1; 
  cin >> n2;

  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    cin >> first; cin >> second;
    cout << n1 + " " + n2 << endl; 
    if (first == n1) {
      n1.assign(second); 
    } else if (first == n2) {
      n2.assign(second);
    }
  }
  cout << n1 + " " + n2 << endl; 
  return 0;
}
