function solution(priorities, location) {
    var answer = 0;
    var copyPrior = [...priorities];
    var dataMap = priorities.map((prior,index)=>({prior,index}));
    
    console.log(dataMap.length);
    while(dataMap.length !== 0){
        var max = Math.max(...copyPrior);
        var {prior, index} = dataMap.shift();
        if(max <= prior){
            answer++;
            copyPrior[index] = 1;
            
            if(index === location){
                break;
            }
        }else{
            dataMap.push({prior,index});       
        }
    }
    
    return answer;
}

