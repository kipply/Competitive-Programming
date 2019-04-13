#include <bits/stdc++.h>

using namespace std;

int n; 

int main(){
  scanf("%d", &n);
  int s = n / 2.0 * (n + 1); 

  for (int i = 2; i < n + 1; i++) {
    if (!(s % i)) {
      cout << "Yes" << endl;
      printf("1 %d\n%d ", i, n - 1); 
      for (int j = 1; j < n + 1; j++) {
        if (j != i) printf("%d ", j); 
      }
      return 0;
    }
  }
  cout << "No";
  return 0;
}