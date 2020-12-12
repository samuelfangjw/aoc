#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;

// Part 1 Variables
int NS1 = 0;
int EW1 = 0;
int direction = 1; //North, East, South, West
vector<int> dirNS = {1, 0, -1, 0};
vector<int> dirEW = {0, 1, 0, -1};

// Part 2 Variables
int NS2 = 1;
int EW2 = 10;
int shipNS = 0;
int shipEW = 0;

void solve(char c, int d) {
    if (c == 'N') {
        NS1 += d;
        NS2 += d;
    }

    if (c == 'S') {
        NS1 -= d;
        NS2 -= d;
    }

    if (c == 'E') {
        EW1 += d;
        EW2 += d;
    }

    if (c == 'W') {
        EW1 -= d;
        EW2 -= d;
    }

    if (c == 'F') {
        NS1 += dirNS[direction] * d;
        EW1 += dirEW[direction] * d;

        shipNS += (NS2 * d);
        shipEW += (EW2 * d);
    }

    if (c == 'L') {
        d /= 90;
        direction += (4-d);
        direction %= 4;

        while (d--) {
            int temp = EW2;
            EW2 = -NS2;
            NS2 = temp;
        }
    }

    if (c == 'R') {
        d /= 90;
        direction += d;
        direction %= 4;

        while (d--) {
            int temp = EW2;
            EW2 = NS2;
            NS2 = -temp;
        }
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;

    while (cin >> s) {
        char c = s[0];
        int d = stoi(s.substr(1));

        solve(c, d);
    }

    cout << "Part 1:\n";
    cout << abs(EW1) + abs(NS1) << "\n\n";
    cout << "Part 2:\n";
    cout << abs(shipEW) + abs(shipNS);
}