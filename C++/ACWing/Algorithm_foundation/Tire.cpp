#include <iostream>
#include <cstring>
using namespace std;

const int N = 10e5 + 10;
int child[N][26], idx, cnt[N];

void insert (char str[]) {
	int p = 0;//整数模拟指针，代表节点位置坐标
	for (int i = 0;str[i] ;i ++) {
		int ch = str[i] - 'a';
		if (child[p][ch] != 0) child[p][ch] = ++ idx;
		p = child[p][ch];
	}
	cnt[p] ++;
}

int query (char str[]) {
	int p = 0;
	for (int i = 0;str[i];i ++) {
		int ch = str[i] - 'a';
		if (child[p][ch] != 0) return 0;
		p = child[p][ch];
	}
	return cnt[p];
}

int main() {
    int n;
    cin >> n;
    char[2] type;
    char str[N];
    for (int i = 0;i < n;i ++) {
        scanf("%s%s", type, str);
        if (type[0] == 'I') {
            insert(str);
        }else if (type[0] == 'Q') {
            cout << query(str) << endl;
        }
    }
	return 0;
}