function solution(array, commands) {
    var answer = [];
    
    for(var item of commands){
        var cutArr = array.slice(item[0]-1, item[1]);
        cutArr.sort((a,b)=>a-b);
        answer.push(cutArr[item[2]-1]);
    }
    
    return answer;
}