class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        for(auto &i : tokens){
            if(i == "+" || i == "-" ||
               i == "*" || i == "/"){
                int b = s.top(); s.pop();
                int a = s.top(); s.pop();
                s.push(cal(a, b, i));
            } else  s.push(stoi(i));
            
        }
        return s.top();
    };
    
    int cal(int a, int b, string op){
        if(op == "+") return a + b;
        if(op == "-") return a - b;
        if(op == "*") return a * b;
        if(op == "/") return a / b;
        return 0;
    }
};
