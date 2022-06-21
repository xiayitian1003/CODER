#include <iostream>
using namespace std;
const int N = 10e5 + 10;
int a[N], father[N];

void init(int n) {
    for (int i = 0;i <= n;i ++) {
        father[i] = i;
    } 
}

int find(int a) {
    if (father[a] != a) father[a] = find(father[a]);
    return father[a];
}

bool query(int a, int b) {
    return find(a) == find(b);
}

int main(){
    int n, m;
    cin >> n >> m;
    init(n);
    
    for (int i = 0;i < m;i ++) {
        char op[2];
        int a, b;
        scanf("%s%d%d", op, &a, &b);
//        printf("op1: %c, op2: %c, a = %d, b = %d\n", op[0], op[1], a, b);
		if (op[0] == 'M') {
		    father[find(a)] = find(b);
		    
		}else if (op[0] == 'Q') {
		    cout << (query(a, b)? "Yes" : "No") << endl;
		}
    }
    
    return 0;
}