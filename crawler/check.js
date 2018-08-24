const request = require('request');
const childProcess = require('child_process');
const fs = require('fs')

let maxId = 506

let map = new Map()

let data = fs.readFileSync('zi.txt')
data = data.toString().trim().split('\n,')

data = data.map(_ => {
    return JSON.parse(_)
})
console.log(data[0])


let index = 1
data = data.map(_ => {
    return {
        id: index++,
        titleList: _.Title.map(__ => __.Title),
        signIndex: _.Title.findIndex(_ => _.IsSign),
        answerList: _.Answer.map(__ => __.Answer),
        correctIndex: _.Index
    }
})

let dataTo = data.filter(_ => {
    return _.id >= 1 && _.id <= 884 || _.id >= 972 && _.id <= 1361
})
let dataTh = data.filter(_ => {
    return _.id >= 1362 && _.id <= 1436 || _.id >= 885 && _.id <= 971
})

index = 1

data = {
    degree1: dataTo.map(_ => {
        _.id = index++
        return _
    }),
    degree2: dataTh.map(_ => {
        _.id = index++
        return _
    })
}

// fs.writeFileSync('checked.txt', data.reduce((a, b) => a + b))
fs.writeFileSync('quizBase.json', JSON.stringify(data))


// {"Id":"2","Title":[{"Title":"气","IsSign":0},{"Title":"?","IsSign":1}],"Answer":[{"Id":"","Answer":"概"},{"Id":"","Answer":"慨"}],"TimeLong":10,"Index":0}
// quiz.id,
// titleList,
// answerList
// correctIndex