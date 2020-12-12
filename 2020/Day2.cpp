#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string a, b, c;
    int p1result = 0;
    int p2result = 0;

    while (cin >> a) {
        cin >> b >> c;

        auto dash = a.find('-');
        int from = stoi(a.substr(0, dash));
        int to = stoi(a.substr(++dash));
        int count = 0;

        for (char ch : c) {
            if (ch == b[0]) {
                count++;
            }
        }

        if (count <= to && count >= from) {
            p1result++;
        }

        if (c[to-1] == b[0] ^ c[from-1] == b[0]) {
            p2result++;
        }
    }

    cout << "Part 1:\n";
    cout << p1result << "\n\n";
    cout << "Part 2:\n";
    cout << p2result;

}
