function solution(phone_book) {
    var answer = true;
    var dataArr = phone_book.sort();
    var size = dataArr.length;
    for(var i=0; i<size-1; i++){
        if(dataArr[i+1].startsWith(dataArr[i])) return false;
    }
    return answer;
}

// function solution(phone_book) {
//     var answer = true;
//     var dataArr = phone_book.sort((a,b)=>a-b);
        
//     for(var i=0; i<dataArr.length-1; i++){
//         for(var j=i+1; j<dataArr.length;j++){
//             const a = dataArr[i].toString();
//             const b = dataArr[j].toString();
//             console.log(a + ', ' + b + ', result : ' + a.startsWith(b));
//             if(a.startsWith(b)){
//                 return false;
//             }
//         }
//     }
//     return answer;
// }
// function solution(phone_book) {
//     var answer = true;
//     var dataArr = phone_book.sort((a,b)=>a-b);
//     var dataMap = new Map();
    
//     for(var obj=0; obj<phone_book.length;){
//         var tempData = dataArr.shift();
//         var len = tempData.length;
//         for(var i=1; i<len;i++){
//             const data = tempData.slice(0, i);
//             if(dataMap.has(data)) return false;
//         }
//         dataMap.set(tempData);
//     }
//     return answer;
// }

//function solution(phone_book) {
//    var answer = true;
//    var dataArr = phone_book.sort((a,b)=>a-b);
//    
//    for(var obj=0; obj<phone_book.length-1;){
//        var tempData = dataArr.shift();
//        var len = tempData.length;
//        var dataMap = new Set(dataArr.map(item=>item.slice(0,len)));
//        if(dataMap.has(tempData) !== false) return false;
//    }
//    return answer;
//}

// function solution(phone_book) {
//     var answer = true;
//     var dataArr = phone_book.sort((a,b)=>a-b);
//     var size = dataArr.length;
//     for(var i=0; i<size; i++){
//         var val = dataArr.shift();
//         for(item of dataArr){
//             if(item.startsWith(val)) return false;
//         }
//     }
//     return answer;
// }