function solution(numbers) {
    var answer = '';
    numbers.sort(function(a,b){
        var ab = Number(a + '' + b);
        var ba = Number(b + '' + a);
        return ba - ab;
    });
    if(numbers[0] !== 0){
        numbers.forEach(item=>{
            answer = answer + '' + item;
        })
    }else answer='0';
    
    return answer;
}