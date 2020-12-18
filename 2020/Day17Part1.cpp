#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;

int arrSize = 20;
int centerIdx = 10;

char v[20][20][20];
queue<tuple<int, int, int, char>> changes;

void processChanges() {
    while (!changes.empty()) {
        auto& [x,y,z,c] = changes.front();
        v[x][y][z] = c;
        changes.pop();
    }
}

int checkCell(int x, int y, int z) {
    if (x < 0 || y < 0 || z < 0 || x >= arrSize || y >= arrSize || z >= arrSize) {
        return 0;
    }

    if (v[x][y][z] == '#') {
        return 1;
    } else {
        return 0;
    }
}

int countActive(int x, int y, int z) {
    int active = 0;
    int d[] = {-1, 0, 1};

    for (int i : d) {
        for (int j : d) {
            for (int k : d) {
                active += checkCell(x + i, y + j, z + k);
            }
        }
    }
    
    return active;
}

void solve() {
    for (int x = 0; x < arrSize; x++) {
        for (int y = 0; y < arrSize; y++) {
            for (int z = 0; z < arrSize; z++) {
                if (v[x][y][z] == '#') {
                    int active = countActive(x,y,z) - 1;
                    if (active != 2 && active != 3) {
                        changes.push({x,y,z,'.'});
                    };
                } else {
                    int active = countActive(x,y,z);
                    if (active == 3) {
                        changes.push({x,y,z,'#'});
                    };
                }
            }
        }
    }
}
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Initialise 3d array
    for (int i = 0; i < arrSize; i++) {
        for (int j = 0; j < arrSize; j++) {
            for (int k = 0; k < arrSize; k++) {
                v[i][j][k] = '.';
            }
        }
    }

    // Read Input
    string s;
    int x = 0;
    int offset = centerIdx - 4;
    while(cin >> s) { 
        for (int y = 0; y < s.size(); y++) {
            if (s[y] == '#') {
                v[x + offset][y + offset][offset] = '#';
            }
        }
        x++;
    }

    // Simulate Cycles
    int n = 6;
    while (n--) {
        solve();
        processChanges();
    }

    //Count cubes
    int part1 = 0;
    for (int i = 0; i < arrSize; i++) {
        for (int j = 0; j < arrSize; j++) {
            for (int k = 0; k < arrSize; k++) {
                if (v[i][j][k] == '#') {
                    part1++;
                }
            }
        }
    }

    cout << part1;

}