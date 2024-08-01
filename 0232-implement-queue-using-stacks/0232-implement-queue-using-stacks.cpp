
class MyQueue {
public:
    stack<int> s;
    MyQueue() {
        
    }
    
    void push(int x) {
        s.push(x);
    }
    
    int pop() {
        stack<int> tmp;
        while (s.size() > 1) {
            tmp.push(s.top());
            s.pop();
        }

        int ans = s.top();
        s.pop();
        while (!tmp.empty()) {
            s.push(tmp.top());
            tmp.pop();
        }
        return ans;
    }
    
    int peek() {
        stack<int> tmp;
        while (s.size() > 1) {
            tmp.push(s.top());
            s.pop();
        }

        int ans = s.top();
        while (!tmp.empty()) {
            s.push(tmp.top());
            tmp.pop();
        }
        return ans;
    }
    
    bool empty() {
        return s.empty();
    }
};


/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */