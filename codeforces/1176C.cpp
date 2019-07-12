#include <bits/stdc++.h>

using namespace std;

int n, a[500001]; 

int ans; 
int nums[43]; 
int found[6]; 

int main(){
  nums[4] = 0; 
  nums[8] = 1; 
  nums[15] = 2; 
  nums[16] = 3;
  nums[23] = 4; 
  nums[42] = 5; 


  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
    int idx = nums[a[i]]; 
    if (idx == 0) {
      found[0]++; 
    } else if (found[idx - 1]) {
      found[idx - 1]--; 
      found[idx]++;
    }
  }
  ans = n - found[5] * 6;
  if (ans < 0) ans = n; 
  cout << ans << endl;


  return 0;
}
