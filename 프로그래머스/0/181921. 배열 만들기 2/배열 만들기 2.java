import java.util.*;
class Solution {
    public int[] solution(int l, int r) {
        List<Integer> list = new ArrayList<>();
  
        for(int i=l; i <= r ;i++){
            String strI = i+"";
            String[] strIArr = strI.split("");
            
            int strLength = 0;
            for(String s : strIArr){
                if(s.equals("0") || s.equals("5")) strLength++;
            }
            
            if(strLength == strIArr.length) list.add(i);
        }

        if(list.size()==0) list.add(-1);
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}

// 5, 5*10. 5*10+5, 5*100, 5*100+5, 5*100 +5 + 5*10, 5*100 + 5 + 5*10 + 5
// i=l ~ r 이전까지의 0과 5로 이루어진 수...
// 반복돌리면서 i가 0과 5로 이루어져 있는지 확인
// -> i를 문자열로 바꾼후 split하는데,
//boolean flag = false;
// -> for 문자열 배열 if(!i.euqals(0) || !i.equals(5)) flag = false, continue;;
//          flag = true
// 배열을 다 순회하고 나서도 flag가 true면 0과 5로만 이루어져 있음. 따라서 해당 i를 리스트에 저장. 
//리스트를 int[]로 변환. 