#include <bits/stdc++.h>

using namespace std;
double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    int n1 = nums1.size();
    int n2 = nums2.size();
    if (n2 < n1) { 
        return findMedianSortedArrays(nums2, nums1); 
    }
    
    int lo = 0; 
    int hi = n1 * 2; 
    
    while (lo <= hi) {
        int cut1 = (lo + hi + 1) / 2; 
        int cut2 = n1 + n2 - cut1; 
        
        int l1, l2, r1, r2; 
        
        if (cut1 == 0) {
            l1 = - (1 << 30); 
        } else {
            l1 = nums1[cut1 - 1]; 
        }
                    
        if (cut2 == 0) {
            l2 = - (1 << 30); 
        } else {
            l2 = nums1[cut2 - 1]; 
        }
        
        if (cut1 == n1 - 1) {
            r1 = 1 << 30; 
        } else {
            r1 = nums1[cut1 + 1]; 
        }
        
        if (cut2 == n2 - 1) {
            r2 = 1 << 30; 
        } else {
            r2 = nums1[cut2 + 1]; 
        }
        
        if (l1 >= r2) {
            lo = cut1; 
        } else if (l2 >= r1) {
            hi = cut1 - 1; 
        } else {
            return (max(l1, l2) + min(r2, r1)) / 2;
        }
    }
    return -1;
}

int main() {
    vector<int> a, b; 
    a.push_back(1);
    b.push_back(2); b.push_back(2);

    cout << findMedianSortedArrays(a, b);

}