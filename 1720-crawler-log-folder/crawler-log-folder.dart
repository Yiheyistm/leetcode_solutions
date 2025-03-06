class Solution {
  int minOperations(List<String> logs) {
    List<String> stk = [];
    for(String log in logs){
        if (log == './') continue;
        else if (log == '../'){
            if (stk.length > 0){
                stk.removeLast();
            }
        }
        else{
            stk.add(log);
        }
    }
    return stk.length;

    
  }
}