#include <bits/stdc++.h>

using namespace std;

int n, p[1001], holes[1001];

int main(){
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &p[i]);
  }

  for (int i = 0; i < n; i++) {
    memset(holes, 0, 1001);
    int curr = i; 
    while (true) {
      if (holes[curr]) {
        cout << curr + 1; 
        cout << " "; 
        break;
      }
      holes[curr] = 1; 
      curr = p[curr] - 1; 
    }
  }

  return 0;
}
