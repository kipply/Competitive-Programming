#include <bits/stdc++.h>

using namespace std;

int n, grades[101], ans;

int main(){
  scanf("%d", &n); 
  for (int i = 0; i < n; i++) {
    scanf("%d", &grades[i]);
  }
  sort(grades, grades + n);
  for (int i = 0; i < n; i++) {
    int sum = 0; 
    for (int j = 0; j < n; j++) {
      sum += grades[j]; 
    } 

    if (round(sum * 1.0 / n) == 5.0) {
      break;
    }

    ans++; 
    grades[i] = 5; 
  }

  cout << ans;
  return 0;
}
