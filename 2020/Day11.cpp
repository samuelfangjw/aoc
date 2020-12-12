#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;
 
vector<string> v1;
vector<string> v2;
vector<string> v3;
bool same = false;

// Part 1 Functions
int checkAdj1(int i, int j) {
    int count = 0;

    vector<int> ni = {1, 1, 1, 0, 0, -1, -1, -1};
    vector<int> nj = {1, -1, 0, -1, 1, -1, 1, 0};

    for (int k = 0; k < 8; k++) {
        int ii = ni[k] + i;
        int jj = nj[k] + j;
        if (ii >= 0 && jj >= 0 && ii < v1.size() && jj < v1[0].length()) {
            if (v1[ii][jj] == '#') {
                count++;
            }
        }
    }

    return count;
}

void solve1() {
    v3.resize(v1.size(), "");
    for (int i = 0; i < v1.size(); i++) {
        string s;
        for (int j = 0; j < v1[0].length(); j++) {
            if (v1[i][j] == '.') {
                s += ".";
            } else if (v1[i][j] == 'L') {
                if (checkAdj1(i, j) == 0) {
                    s += "#";
                } else {
                    s += "L";
                }
            } else {
                if (checkAdj1(i, j) >= 4) {
                    s += "L";
                } else {
                    s += "#";
                }
            }
        }
        v3[i] = s;
    }

    same = true;
    for (int k = 0; k < v1.size(); k++) {
        if (v1[k].compare(v3[k]) != 0) {
            same = false;
        }

        v1[k] = v3[k];
    }
}

// Part 2 Functions
int checkAdj2(int i, int j) {
    int count = 0;
    
    vector<int> ni = {1, 1, 1, 0, 0, -1, -1, -1};
    vector<int> nj = {1, -1, 0, -1, 1, -1, 1, 0};

    for (int k = 0; k < 8; k++) {
        int ii = ni[k] + i;
        int jj = nj[k] + j;

        loop:

        if (ii >= 0 && jj >= 0 && ii < v2.size() && jj < v2[0].length()) {
            if (v2[ii][jj] == '#') {
                count++;
            } else if (v2[ii][jj] == '.') {
                ii += ni[k];
                jj += nj[k];
                goto loop;
            }
        }
    }

    return count;
}

void solve2() {
    v3.resize(v2.size(), "");
    for (int i = 0; i < v2.size(); i++) {
        string s;
        for (int j = 0; j < v2[0].length(); j++) {
            if (v2[i][j] == '.') {
                s += ".";
            } else if (v2[i][j] == 'L') {
                if (checkAdj2(i, j) == 0) {
                    s += "#";
                } else {
                    s += "L";
                }
            } else {
                if (checkAdj2(i, j) >= 5) {
                    s += "L";
                } else {
                    s += "#";
                }
            }
        }
        v3[i] = s;
    }

    same = true;
    for (int k = 0; k < v2.size(); k++) {
        if (v2[k].compare(v3[k]) != 0) {
            same = false;
        }

        v2[k] = v3[k];
    }
}

// Driver Method
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    while (cin >> s) {
        v1.push_back(s);
        v2.push_back(s);
    }

    while(!same) {
        solve1();
    }

    same = false;

    while(!same) {
        solve2();
    }

    int count1 = 0;
    int count2 = 0;
    for (int i = 0; i < v1.size(); i++) {
        for (int j = 0; j < v1[0].length();j++) {
            if (v1[i][j] == '#') {
                count1++;
            }
            if (v2[i][j] == '#') {
                count2++;
            }
        }
    }

    cout << "Part 1:\n";
    cout << count1 << "\n\n";
    cout << "Part 2:\n";
    cout << count2;
}