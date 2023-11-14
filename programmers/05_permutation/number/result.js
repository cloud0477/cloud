function solution(numbers) {
    var answer = 0;
    var numArr = [...numbers].map((item)=>item*1);
    const result = new Map();
    
    numArr.forEach((item,idx, origin)=>{
        const arr = getPermutations(numArr,numArr.length-idx);
        arr.map(item=>result.set(item.join('')*1,''));
    })
    
    console.log(result);
    for(var item of result.keys()){
        if(item == 1 || item == 0) continue;
        var i=2;
        var bool = true;
        while(i*i <= item){
            if(item % i == 0){
                bool = false;
                break;
            }
            i++;
        }
        if(bool) answer++;
    }
    console.log(answer);

    return answer;
}


const getPermutations= function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((value) => [value]);
  
    arr.forEach((fixed, index, origin) => {
      const rest = [...origin.slice(0, index), ...origin.slice(index+1)] 
      const permutations = getPermutations(rest, selectNumber - 1); 
      const attached = permutations.map((permutation) => [fixed, ...permutation]);
      results.push(...attached); 
    });
  
    return results;
  };

solution([1,7]);