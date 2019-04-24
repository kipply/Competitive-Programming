#include <bits/stdc++.h>

using namespace std;

int n, k, a[100005]; 

int main(){
  scanf("%d %d", &n, &k); 

  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]); 
  }

  sort(a, a + n); 
  int curr = 0; 
  int subtractions = 0; 
  for (int i = 0; i < k; i++) {
    while (a[curr] - subtractions <= 0 && curr < n) {
      curr++; 
    }
    printf("%d\n", max(a[curr] - subtractions, 0));

    subtractions += a[curr] - subtractions; 
  }
  return 0;
}
