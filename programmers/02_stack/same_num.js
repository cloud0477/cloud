function solution(arr)
{
    var answer = [];
    answer.push(arr[0]);
    console.log('test');
    for(var temp=1; temp < arr.length; temp++){
        if((arr[temp-1] == arr[temp])) {
            continue;
        }else{
            answer.push(arr[temp]);
        }
    }
    
    return answer;
}

