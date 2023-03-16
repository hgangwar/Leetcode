#include <iostream>
#include <vector>
using namespace std;

class Solution {
    public:
        int findKthPositive(vector<int>& arr, int k) {
            int ld=0,md=0;
            for (int i=0; i<arr.size(); i++){      
                int diff=(arr[i]-ld-1);      
                if ( md+diff>=k){
                    return (ld+(k-md));                
                }
                md+=diff;
                ld=arr[i];
                
            }
            return (arr.back()+(k-md));
        }
};
int main(){
    Solution obj;
    int arr[] = {2,3,4,7,11};
    vector <int> vect{2,3,4,7,11};
    int k = 5;
    int Ans=obj.findKthPositive(vect, k);
    cout<<"\n Kth missing number is :"<<Ans;
    return 0;
}