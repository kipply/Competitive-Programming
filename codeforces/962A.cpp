#include <bits/stdc++.h>
#include <stdio.h>

using namespace std;

int n, a[200001], sum;

int main(){
  scanf("%d", &n); 
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
    sum += a[i];
  }
  int curr = 0;
  for (int i = 0; i < n; i++) {
    curr += a[i]; 
    if (curr * 1.0 / sum >= 0.5) {
      cout << i + 1; 
      break;
    }
  }
  return 0;
}
