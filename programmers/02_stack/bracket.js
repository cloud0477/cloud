function solution(s){
    var h = 0;
    var j = 0;
    
    if(s[0] == ')') return false;
    if(s[s.length-1] == '(') return false;
    
    for(var i = 0 ; i < s.length; i++){
        if(s[i] == '(')
            h++;
        else
            h--;
        if(h<0) return false;
    }
    if(h>0) return false;
    
    return true;
}
