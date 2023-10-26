function solution(participant, completion) {
    var answer = '';
    var obj = new Object();
    for(item of completion){
        if(obj[item] == undefined) obj[item] = 0;
        else obj[item] = obj[item] + 1;
    }
    
    for(item of participant){
        if(obj[item] >= 0) obj[item] = obj[item] - 1;
        else{
            answer = item;
            break;
        }
    }
    
    return answer;
}