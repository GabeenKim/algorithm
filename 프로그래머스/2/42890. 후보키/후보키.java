import java.util.*;
class Solution {
    static int answer;
    static int n,m;
    static List<HashSet<Integer>> candidateKey;
    static String[][] relationCopy;
    public int solution(String[][] relation) {
        answer = 0;
        relationCopy = relation;
        
        candidateKey = new ArrayList<>();
        n = relation.length;
        m = relation[0].length;
        
        for(int i=1;i<m+1;i++){
            combination(0,i,0,new HashSet<>());
        }
        return answer;
    }
    
    public void combination(int idx, int size, int depth, HashSet<Integer> set){
        //조합이 생성되면 
        if(depth == size){
            //최소성 검사 
            for(HashSet<Integer> key : candidateKey){
                if(set.containsAll(key)) 
                    return;
            }
            //유일성 검사
            if(!isUnique(set))
                return;
            
            candidateKey.add(set);
            answer++;
            return;
        }
        
        for(int i=idx; i<m;i++){
            HashSet<Integer> newSet = new HashSet<>(set);
            newSet.add(i);
            combination(idx+1,size,depth+1,newSet);
        }
    }
    public boolean isUnique(HashSet<Integer> set){
        List<String> list = new ArrayList<>();
        //만들어진 컬럼 조합의 튜플 값들이 중복되는지 검사
        for(int i=0; i<n;i++){
            StringBuilder sb = new StringBuilder();
            for(int idx :set){
                sb.append(relationCopy[i][idx]);
            }
            if(!list.contains(sb.toString())) list.add(sb.toString());
            else return false;
        }
        return true;
    }
    
}