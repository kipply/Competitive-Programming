#include <bits/stdc++.h>

using namespace std;

int n, m, c[1001], cute[1001]; 

int main(){
  scanf("%d %d", &n, &m);
  for (int i = 0; i < m; i++) {
    scanf("%d", &c[i]);
    cute[c[i] - 1]++; 
  }
  cout << *min_element(cute, cute + n);
  return 0;
}