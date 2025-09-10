class Solution {
    public int solution(int n) {
        return getLCM(n,6)/6;
    }
    public int getLCM(int a, int b) {
        return a * b / getGCD(a, b);
    }
    public int getGCD(int a, int b){
        while(b!=0){
            int temp = a%b;
            a = b;
            b= temp;
        }
        return a;
    }
}