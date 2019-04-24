
#include <bits/stdc++.h>

using namespace std;

unsigned long long int n, b[100005], a[200005]; 

int main(){
  scanf("%lld", &n); 
  for (int i = 0; i < n / 2; i++) {
    scanf("%lld", &b[i]);

    unsigned long long int end; 
    if (i == 0) {
      end = b[i];
    } else {
      end = min(a[n - i], b[i]); 
      end = min(end, b[i] - a[i - 1]);
    }

    a[i] = b[i] - end; 
    a[n - i - 1] = end; 
  }


  for (int i = 0; i < n; i++) {
    printf("%lld ", a[i]);
  }
  return 0;
}
