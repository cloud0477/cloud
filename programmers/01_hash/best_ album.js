function solution(genres, plays) {
    var answer = [];
    var dataMap = new Map();
    for(var i=0; i<genres.length; i++){
        var val = plays[i];
        //1: 최대값, 2: 두번째최대값, 3: 1번의인덱스, 4: 2번의 인덱스, sum: 해당장르 총합
        if(dataMap.has(genres[i])){
            var tempArr = dataMap.get(genres[i]);
            var sum = tempArr['sum']+val;
            if(val > tempArr[1]){
                    tempArr[2] = tempArr[1];
                    tempArr[4] = tempArr[3];
                    tempArr[1] = val;
                    tempArr[3] = i;
            }else{
               if(tempArr[2] === undefined){
                    tempArr[2] = val;
                    tempArr[4] = i;
                }else if(val > tempArr[2]){
                    tempArr[2] = val;
                    tempArr[4] = i;
                }
            }
            tempArr['sum'] = sum;
            dataMap.set(genres[i],tempArr);
        }else {
            var tempArr = {};
            tempArr['sum']= val;
            tempArr[1]= val;
            tempArr[3]= i;
            dataMap.set(genres[i],tempArr);
        }
    }
    var arr = [...dataMap]
    var temp = arr.sort((a,b)=>{
        if(a[1].sum > b[1].sum ) return -1;
        if(a[1].sum < b[1].sum ) return 1;
        return 0;
    });
    
    for(item of temp){
        answer.push(item[1][3]);
        if(item[1][4] !== undefined) answer.push(item[1][4]);
    }
    
    return answer;
}