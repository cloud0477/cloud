function solution(k, dungeons) {
    let answer = 0;
    const visited = Array(dungeons.length).fill(false)
    const dfs = (fatigue, count) => {
        console.log('dfs 시작!!');
        answer = Math.max(answer, count)
        for (let i = 0; i < dungeons.length; i++) {
            console.log('i : ', i, ', fatigue - dungeons[i][1] : ', fatigue - dungeons[i][1], ', dungeons[i][0] : ', dungeons[i][0] , ', !visited[i] : ' , !visited[i]);
            if (!visited[i] && fatigue >= dungeons[i][0]) {
                visited[i] = true
                dfs(fatigue - dungeons[i][1], count + 1)
                visited[i] = false
            }
        }
    }
    dfs(k, 0)
    
    return answer;
}

solution(80,[[80,20],[50,40],[30,10]]);