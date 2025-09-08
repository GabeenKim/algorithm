class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        
        int numerator = numer1*denom2 + numer2*denom1;
        int denominator = denom1 * denom2;
        
        int gcd = getGCD(numerator, denominator);
        
        answer[0] = numerator/gcd;
        answer[1] = denominator/gcd;
        
        return answer;
    }
    public int getGCD(int a, int b){
         while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}
