function solution(k, dungeons) {
    var answer = 0;
    var cnt = 0;
    var cases = getPermutation(dungeons,dungeons.length);

    cases.forEach((arr, idx)=>{
        var fatigue = k;
        var tmpCnt = 0;
        for(item of arr){
            if(fatigue >= item[0]){
                fatigue -= item[1];
                tmpCnt++;
            }else{
                break;
            }
        }
        if(tmpCnt > answer) answer = tmpCnt;
    });

    console.log(answer);

    return answer;
}

const getPermutation = (arr,selectNum)=>{
    const results = [];
    if(selectNum === 1){
        const results = arr.map(item=>[item]);
        console.log(results);
        return results;
    }
    
    arr.forEach((item,idx,origin)=>{
        const reset = [...origin.slice(0,idx), ...origin.slice(idx+1)];
        const permutations = getPermutation(reset, selectNum-1);
        const attacted = permutations.map(value=>[item, ...value]);
        results.push(...attacted);
    })

    return results;
}

solution(80,[[80,20],[50,40],[30,10]]);