#include <bits/stdc++.h>

using namespace std;

int r, c; 
char cactus[501][501]; 

int dx[] = {1, -1, 0, 0}; 
int dy[] = {0, 0, -1, 1}; 

int main(){
  string ans = "Yes"; 

  scanf("%d %d", &r, &c);

  for (int i = 0; i < r; i++) {
    scanf("%s", cactus[i]); 
  }

  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      if (cactus[i][j] == 'S') {
        for (int x = 0; x < 4; x++) {
          if (cactus[i + dx[x]][j + dy[x]] == 'W') {
            ans = "No"; 
          } else if (cactus[i + dx[x]][j + dy[x]] == '.') {
            cactus[i + dx[x]][j + dy[x]] = 'D'; 
          }
        }
      }
    }
  }

  if (ans == "No") {
    cout << ans; 
  } else {
    cout << ans << endl; 
    for (int i = 0; i < r; i++){
      cout << cactus[i] << endl; 
    }
  }
  return 0;
}


