function solution(clothes) {
    var answer = 1;
    var dataMap = new Map();
    for(item of clothes){
        if(dataMap.has(item[1])){
            dataMap.set(item[1], dataMap.get(item[1]) + 1);
        }else{
            dataMap.set(item[1], 2);
        }
    }
    for(item of dataMap.values()){
        answer *= item;
    }
    
    return answer - 1;
}