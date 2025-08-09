import java.util.*;
class Solution {
    static int row,col;
    static List<HashSet<Integer>> candidateKeys = new ArrayList<>();
    static String[][] relation;
    
    public int solution(String[][] relation) {
        this.relation = relation;
        this.row = relation.length;
        this.col = relation[0].length;
        
        //1개의 컬럼부터 모든 컬럼가지의 조합 시도
        for(int i=1; i<=col; i++){
            combination(0,i,new HashSet<>());
        }
        return candidateKeys.size();
    }
    
    private  void combination(int start, int size, Set<Integer> currentCombination){
        //조합이 완성되면
        if(currentCombination.size() == size){
            if(isMinimal(currentCombination)){
                if(isUnique(currentCombination)){
                    candidateKeys.add(new HashSet<>(currentCombination));
                }
            }
           return;
        }
        
        //재귀 호출
        for(int i=start; i< col;i++){
            currentCombination.add(i);
            combination(i+1,size,currentCombination);
            currentCombination.remove(i); //재귀 후 원상복구
            
        }
    }
    
    //최소성 검사
    private boolean isMinimal(Set<Integer> combination){
        for(Set<Integer> key : candidateKeys){
            //기존 후보키가 현재 조합의 부분 집합이라면 최소성 만족X
            if(combination.containsAll(key)) return false;
        }
        return true;
    }
    
    //유일성 검사
    private  boolean isUnique(Set<Integer> combination){
        Set<String> tupleSet = new HashSet<>();
        //만들어진 컬럼 조합의 튜플 값들이 중복되는지 검사
        for(int r=0; r < row ; r++){
            StringBuilder sb = new StringBuilder();
            for(int c :combination){
                sb.append(relation[r][c]).append(",");
            }
            if(!tupleSet.add(sb.toString())) 
                return false;
        }
        return true;
    }
    
}