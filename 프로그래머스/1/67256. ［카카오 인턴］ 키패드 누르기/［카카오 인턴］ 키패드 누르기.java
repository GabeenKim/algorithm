import java.util.*;
class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int leftNum = 10;
        int rightNum = 12;
        
        for(int num : numbers){
            if(num == 1 || num == 4 || num == 7) {
                answer+="L";
                leftNum = num; 
            }else if(num == 3|| num==6 || num==9) {
                answer+="R";
                rightNum = num;
            }else{
                if(num == 0 ) num = 11;
                int leftDist = Math.abs(num-leftNum)/3 + Math.abs(num-leftNum)%3;
                int rightDist =  Math.abs(num-rightNum)/3 + Math.abs(num-rightNum)%3  ;
                //키패드는 3열로 이루어져 있으므로, 인덱스를 3으로 나눴을 때 나머지 값으로 인덱스를 구할 수 있음. 3으로 나누었을 때 몫은 세로 거리를 나타내고, 나머지는 가로 거리
                if(leftDist < rightDist){
                    answer += "L";
                    leftNum = num ;           
                }else if(leftDist > rightDist){
                    answer += "R";
                    rightNum = num ;
                }else{
                    if(hand.equals("left")){
                        answer += "L";
                        leftNum = num ;
                    }else{
                        answer += "R";
                        rightNum = num ;
                    }
                }
            }

            }
        return answer;
    }
}