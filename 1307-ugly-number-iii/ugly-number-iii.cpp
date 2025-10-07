class Solution {
public:
    long long gcd(long long a, long long b) {
        if (b == 0) {
            return a;
        }
        return gcd(min(a, b), max(a, b) % min(a, b));
    }

    int nthUglyNumber(int n, int a, int b, int c) {
        long long a_ll = a;
        long long b_ll = b;
        long long c_ll = c;

        long long ab = (a_ll / gcd(a_ll, b_ll)) * b_ll;
        long long ac = (a_ll / gcd(a_ll, c_ll)) * c_ll;
        long long bc = (b_ll / gcd(b_ll, c_ll)) * c_ll;
        
        long long abc = (ab / gcd(ab, c_ll)) * c_ll;

        long long low = 0;
        long long high = 2000000000; 
        long long result = 0;

        while (low <= high) {
            long long mid = low + (high - low) / 2;
            
            long long count = (mid / a_ll) + (mid / b_ll) + (mid / c_ll) 
                           - (mid / ab) - (mid / ac) - (mid / bc)
                           + (mid / abc);

            if (count >= n) {
                result = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return static_cast<int>(result);
    }
};
