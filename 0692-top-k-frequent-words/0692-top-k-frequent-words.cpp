class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        map<string,int> m;
        for(auto &i: words){
            m[i] += 1;
        }
        set<pair<int, string>> s;
        for(auto &[i, j]: m){
            s.insert(make_pair(-j, i));
        }
        vector<string> out;
        int c = 0;
        for(auto &it : s){
            if(c<k){
                out.push_back(it.second);
            }
            c++;
        }
        return out;
        
    }
};