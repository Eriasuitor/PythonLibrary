const request = require('request');
const childProcess = require('child_process');
const fs = require('fs')

let maxId = 10

let map = new Map()

let action = new Promise(async (resolve, reject) => {
    while (map.size < maxId) {
        await new Promise((resolve, reject) => {
            request.post({
                url: 'https://guess.apksc.com/v2.0//api/Activity/getAllQuestion.html',
                body: 'phpsessid=96uvdh6uc3sje6cl3f9pots7k6&aid=10098316',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }).on('data', data => {
                data = JSON.parse(data)
                data.Result.Questions.map(_ => {
                    delete _.Number
                    if (Number(_.Id) > Number(maxId)) {
                        maxId = Number(_.Id)
                    }
                    map.set(_.Id, _)
                })
                console.log(`maxId: ${maxId}, map.size: ${map.size}`)
                resolve()
            }).on('error', err => {
                reject(err)
            })
        })
    }
    resolve(1)
})
let countdown = new Promise(resolve => {
    setTimeout(resolve, 300000, 2);
})

Promise.race([countdown, action]).then(async value => {
    console.log(`crawler finished with ${value}`)
    let data = []
    map.forEach(_ => {
        data.push(_)
    })
    data = data.sort((a, b) => Number(a.Id) > Number(b.Id) ? 1 : -1)
    data = data.map(_ => JSON.stringify(_) + '\n')
    await fs.writeFileSync('questions.txt', data)
    console.log(`${data.length} rows was inserted`)
})

