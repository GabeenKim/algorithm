import java.util.HashMap;
class Solution {
    public boolean solution(String[] phone_book) {
        HashMap<String,Integer> hm = new HashMap<>();
        for(int i=0; i<phone_book.length;i++)
            hm.put(phone_book[i],i);
        for(String value : phone_book){
            for(int i=1; i<value.length() ;i++){
                if(hm.containsKey(value.substring(0,i)))
                    return false;
            }
        }
        
        return true;
    }
}