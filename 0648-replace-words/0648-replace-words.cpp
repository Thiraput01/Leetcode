class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        ios_base::sync_with_stdio(false);cin.tie(NULL);
        unordered_set<string> s;
        string word = "", res = "";
        sentence += ' ';
        for(auto &i : dictionary) s.insert(i);
        for(auto &c : sentence){
            if(c == ' '){
                if(res.size() > 0) res += ' ';

                string tmp = "";
                for(auto &i : word){
                    tmp += i;
                    if(s.count(tmp)) break;
                }

                res += tmp;
                word = "";
            } else word += c;
        }
        return res;
    }
};