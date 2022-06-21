#include <iostream>
#include <string>
using namespace std;
const int N = 10e5 + 10;
int a[N], father[N], Size[N];

void init(int n) {
    for (int i = 0;i <= n;i ++) {
        father[i] = i;
        Size[i] = 1;
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
        string op;
        int a, b;
        cin >> op;
        cout << op << endl;
//        printf("op1: %c, op2: %c, a = %d, b = %d\n", op[0], op[1], a, b);
		    if (op == "C")  {
		        cin >> a >> b;
				if (a != b) {
					Size[find(b)] += Size[find(a)];
					father[find(a)] = find(b);
				}
				break;
			}else if (op == "Q1") {
			    cin >> a >> b;
			    cout << (query(a, b)? "Yes" : "No") << endl;
				break;
			}
			else if (op == "Q2") {
			    cin >> a;
				cout << Size[a] << endl;
				break;
			}	
    }
    
    return 0;
}