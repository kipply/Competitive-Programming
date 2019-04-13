#include <bits/stdc++.h>

using namespace std;

int n, m; 

char cactus[101][101]; 
int dr[] = {0, 0, 1, -1, 1, -1, 1, -1}; 
int dc[] = {1, -1, 0, 0, 1, -1, -1, 1}; 

int main(){
  scanf("%d %d\n", &n, &m);
  for (int i = 0; i < n; i++) {
    scanf("%s", cactus[i]);
  }

  string ans = "YES"; 

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (isdigit(cactus[i][j])) {
        int mines = 0; 
        for (int x = 0; x < 8; x++) {
          if (cactus[i + dr[x]][j + dc[x]] == '*') {
            mines++; 
          }
        }
        if (mines != cactus[i][j] - '0') {
          ans = "NO"; 
        }
      }

      if (cactus[i][j] == '.') {
        for (int x = 0; x < 8; x++) {
          if (cactus[i + dr[x]][j + dc[x]] == '*') {
            ans = "NO"; 
          }
        }
      }
    }
  }
  cout << ans << endl;
  return 0;
}
