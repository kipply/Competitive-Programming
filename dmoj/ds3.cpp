#include <bits/stdc++.h>
#define pb push_back
#define left(x) (x << 1)
#define right(x) (x <<  1 | 1)
#define mid(l, r) ((l + r) >> 1)
using namespace std;

struct node{
	int l, r;
	int mini, gcd, c;
	node(){ mini = 0, c = gcd = 1; }
}cactus[300050];

int n, m, vals[300050];

inline int gcd(int a, int b){
	if(b == 0) return a;
	return gcd(b, a % b);
}

inline void calc(int i){
	cactus[i].gcd = gcd(cactus[left(i)].gcd, cactus[right(i)].gcd);
	cactus[i].mini = min(cactus[left(i)].mini, cactus[right(i)].mini);
	cactus[i].c = 0;
	if(cactus[i].gcd == cactus[left(i)].gcd) cactus[i].c += cactus[left(i)].c;
	if(cactus[i].gcd == cactus[right(i)].gcd) cactus[i].c += cactus[right(i)].c;
}

inline void apply(int i, int val){
	cactus[i].mini = cactus[i].gcd = val;
	cactus[i].c = 1;
}

void build(int l, int r, int i){
	cactus[i].l = l, cactus[i].r = r;
	if(l == r) {
		apply(i, vals[l]);
		return;
	}
	build(l, mid(l, r), left(i)), build(mid(l, r) + 1, r, right(i));
	calc(i);
}

void update(int p, int val, int i){
	if(cactus[i].l > p || cactus[i].r < p) return;
	if(cactus[i].l == cactus[i].r){
		apply(i, val);
		return;
	}
	update(p, val, left(i)), update(p, val, right(i));
	calc(i);
}

int minimum(int l, int r, int i){
	if(l < cactus[i].l + 1 && cactus[i].r < r + 1)
	    return cactus[i].mini;
	if(cactus[i].l > r || l > cactus[i].r)
	    return 0x3f3f3f3f;
	return min(minimum(l, r, left(i)), minimum(l, r, right(i)));
}

int greatestCommonFactor(int l, int r, int i){
	if(l < cactus[i].l + 1 && cactus[i].r < r + 1)
	    return cactus[i].gcd;
	if(cactus[i].l > r || l > cactus[i].r)
	    return 0;
	return gcd(greatestCommonFactor(l, r, left(i)), greatestCommonFactor(l, r, right(i)));
}


int cactusCute(int l, int r, int i){
	if(l < cactus[i].l + 1 && cactus[i].r < r + 1)
	    return cactus[i].c;
	if(cactus[i].l > r || l > cactus[i].r)
	    return 0;
	int ll = greatestCommonFactor(l, r, left(i)), rr = greatestCommonFactor(l, r, right(i));
	int all = gcd(ll, rr);
	int res = 0;
	if(all == ll) res += cactusCute(l, r, left(i));
	if(all == rr) res += cactusCute(l, r, right(i));
	return res;
}

int main(){
	scanf("%d%d", &n, &m);
	for(int i = 1; i < n + 1; i++)
	    scanf("%d", vals+i);
	build(1, n, 1);

	char f;
	int a, b;

	for(; m--;){
		scanf(" %c%d%d", &f, &a, &b);
		if(f == 'C') update(a, b, 1);
		else if(f == 'M') printf("%d\n", minimum(a, b, 1));
		else if(f== 'G') printf("%d\n", greatestCommonFactor(a, b, 1));
		else if(f == 'Q') printf("%d\n", cactusCute(a, b, 1));
	}
	return 0;
}
