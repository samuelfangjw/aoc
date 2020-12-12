#include "bits/stdc++.h"
 
using namespace std;
typedef long long ll;

unordered_map<string, unordered_set<string>> um1;
unordered_set<string> part1Result;
unordered_map<string, vector<pair<string, int>>> um2;
unordered_map<string, int> mem;

void solve1(string s) {
    auto us = um1[s];
    part1Result.insert(s);

    for (string t : us) {
        if (part1Result.find(t) == part1Result.end()) {
            solve1(t);
        }
    }
}

int solve2(string s) {
    auto vec = um2[s];

    if (vec.empty()) {
        return 1;
    } 
    
    if (mem.find(s) != mem.end()) {
        return mem[s];
    }

    int count = 1;
    for (auto p : vec) {
        count += solve2(p.first) * p.second;
    }
    mem[s] = count;
    return count;
}
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;

    while (getline(cin, s)) {
        stringstream ss(s);

        string token;
        string bag = "";

        ss >> token;
        bag += token;
        ss >> token;
        bag += token;

        ss >> token;
        ss >> token;
        
        while (ss >> token) {
            if (token.compare("no") == 0) {
                break;
            }
            string bagIn = "";

            int num = stoi(token);
            ss >> token;
            bagIn += token;
            ss >> token;
            bagIn += token;
            ss >> token;

            auto us1 = um1[bagIn];
            us1.insert(bag);
            um1[bagIn] = us1;

            auto us2 = um2[bag];
            us2.push_back({bagIn, num});
            um2[bag] = us2;
        }
    }

    solve1("shinygold");

    cout << "Part 1:\n";
    cout << part1Result.size() - 1 << "\n\n";

    cout << "Part 2:\n";
    cout << solve2("shinygold") - 1;
}