#include <bits/stdc++.h>

using namespace std;

int n, cute[100005]; 

int main(){
  scanf("%d", &n); 
  for (int i = 2; i < n + 2 + 1; i++) {
    if (!cute[i]) {
      for (int j = i * 2;  j < n + 2 + 1; j += i) {
        cute[j] = 1; 
      }
    }
  } 

  printf("%d\n", *max_element(cute + 2, cute + (n + 2)) + 1);
  for (int i = 2; i < n + 2; i++) {
    printf("%d ", cute[i] + 1);
  }
  return 0;
}
