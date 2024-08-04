using namespace std;

class Solution {
public:
    string countOfAtoms(string formula) {
        int n = formula.size();
        stack<map<string, int>> stk;
        stk.push(map<string, int>());
        int i = 0;

        while (i < n) {
            if (formula[i] == '(') {
                stk.push(map<string, int>());
                i++;
            } else if (formula[i] == ')') {
                string countStr = "";
                i++;
                while (i < n && isdigit(formula[i])) {
                    countStr += formula[i];
                    i++;
                }
                int count = (countStr.empty()) ? 1 : stoi(countStr);

                auto curMap = stk.top();
                stk.pop();
                auto &prevMap = stk.top();

                for (auto &entry : curMap) {
                    prevMap[entry.first] += entry.second * count;
                }
            } else {
                string ele = string(1, formula[i]);
                i++;
                if (i < n && islower(formula[i])) {
                    ele += formula[i];
                    i++;
                }

                string countStr = "";
                while (i < n && isdigit(formula[i])) {
                    countStr += formula[i];
                    i++;
                }
                int count = (countStr.empty()) ? 1 : stoi(countStr);

                stk.top()[ele] += count;
            }
        }

        auto resMap = stk.top();
        string result = "";

        for (auto &entry : resMap) {
            result += entry.first;
            if (entry.second > 1) {
                result += to_string(entry.second);
            }
        }

        return result;
    }
};

