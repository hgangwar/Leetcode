#include <iostream>
#include <vector>
#include <string>

using namespace std;
struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };
class Solution {
public:
    void solve(TreeNode* root, vector<int> &ans){
        if(root == NULL)
        return;

        solve(root -> left,ans);
        ans.push_back(root -> val);
        solve(root -> right,ans);

    }
    int getMinimumDifference(TreeNode* root) {
        vector<int> ans; 
        solve(root, ans);
        int min =0; int diff = 100009;
        for(int i=1; i<ans.size(); i++){
            min = ans[i] - ans[i -1];
            if(min < diff){
                diff = min;
            }
        }
        return diff;

    }
};

int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
}