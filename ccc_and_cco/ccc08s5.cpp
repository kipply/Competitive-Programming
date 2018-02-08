#include <bits/stdc++.h>
#include <stdio.h>

using namespace std;

int dp[35][35][35][35];
int reactions[5][4] = {
    {2, 1, 0, 2},
    {1, 1, 1, 1},
    {0, 0, 2, 1},
    {0, 3, 0, 0},
    {1, 0, 0, 1}
};
int n, A, B, C, D, a, b, c, d;
int main(){
    for (int a = 0; a < 31; a++){
        for (int b = 0; b < 31; b++){
            for (int c = 0; c < 31; c++){
                for (int d = 0; d < 31; d++){
                    for (auto reaction: reactions){
                        if (a >= reaction[0] && b >= reaction[1] && c >= reaction[2] && d >= reaction[3]){
                            if (!dp[a - reaction[0]][b - reaction[1]][c - reaction[2]][d - reaction[3]]){
                                dp[a][b][c][d] = 1;
                            }
                        }
                    }
                }
            }
        }
    }
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        scanf("%d %d %d %d", &A, &B, &C, &D);
        if (dp[A][B][C][D]){
            cout << "Patrick\n";
        } else {
            cout << "Roland\n";
        }
    }
}
