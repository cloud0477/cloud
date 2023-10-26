function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    var dataMap = truck_weights;
    const queue = Array.from({length: bridge_length}, () => 0);
    while(true){
        queue.push(0);
        queue.shift();
        
        var sum = queue.reduce(function add(sum,currValue){
                                 return sum + currValue
                               },0);
        
        if(sum + dataMap[0] <= weight){
            var val = dataMap.shift();
            queue[queue.length - 1] = val;
        }
        answer++;
        
        var last = queue.reduce(function add(sum,currValue){
                                 return sum + currValue
                               },0);
        if(last === 0) break;
    }
    return answer;
}