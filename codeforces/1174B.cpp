#include <bits/stdc++.h>

using namespace std;

int n, a[100005]; 

int main(){
  scanf("%d", &n);
  bool cute = false;  
  int remainder = -1; 
  for (int i = 0; i < n; i++) { 
    scanf("%d", &a[i]);
    if (remainder == -1) {
      remainder = a[i] % 2; 
    } else if (a[i] % 2 != remainder) {
      cute = true; 
    }
  }

  if (cute) {
    sort(a, a + n);
  }

  for (int i = 0; i < n; i++) {
    printf("%d ", a[i]);
  }
  return 0;
}

