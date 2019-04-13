#include <bits/stdc++.h>
#include <stdio.h>

using namespace std;

int n;

int main(){
  scanf("%d", &n); 
  
  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
    if (a[i] < 0) {
      neg++;
    } else if (a[i] > 0) {
      pos++; 
    }
  }
  int goal = (n + 1) / 2; 
  if (pos >= goal) {
    printf("1");
  } else if (neg >= goal) {
    printf("-1"); 
  } else {
    printf("0");
  }
  return 0;
}
