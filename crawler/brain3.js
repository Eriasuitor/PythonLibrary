const request = require('request');
const childProcess = require('child_process');
const fs = require('fs')

let maxId = 506

let map = new Map()

let data = fs.readFileSync('questions.txt')

data = data.toString().split('\n,').map(_ => {
    _ = JSON.parse(_)
    map.set(_.Id, _)
})

let action = new Promise(async (resolve, reject) => {
    while (map.size < maxId) {
        await new Promise((resolve, reject) => {
            request.post({
                // url: 'https://guess.apksc.com/v2.0//api/Activity/getAllQuestion.html',
                url: 'https://brain.7759.com/v1.0/api/Activity/getAllQuestion.html',
                body: 'phpsessid=9psvih3h2f2v9qk31n89ougr55&aid=92696326',
                // url: 'https://brain.7759.com/api/Activity/getAnswer.html',
                // body: 'v=4.5&phpsessid=0gotqcrh76f75244r351u4ac82&qid=880',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }).on('data', data => {
                data = JSON.parse(data)
                if (data.Status != 200) {
                    console.log(data)
                    reject('all received')
                }
                else {
                    Promise.all(data.Result.Questions.map(_ => new Promise(resolve => {
                        request.post({
                            url: 'https://brain.7759.com/api/Activity/getAnswer.html',
                            body: `v=4.5&phpsessid=0gotqcrh76f75244r351u4ac82&qid=${_.Id}`,
                            headers: {
                                'Content-Type': 'application/x-www-form-urlencoded'
                            }
                        }).on('data', data => {
                            // console.log(data)
                            resolve(JSON.parse(data).Result)
                        })
                    }))).then(value => {
                        if (value.length != data.Result.Questions.length) reject('unexpected')
                        for (let i = 0; i < value.length; i++) {
                            delete data.Result.Questions[i].Number
                            if (Number(data.Result.Questions[i].Id) > Number(maxId)) {
                                maxId = Number(data.Result.Questions[i].Id)
                            }
                            map.set(data.Result.Questions[i].Id, Object.assign(data.Result.Questions[i], {
                                Result: value[i]
                            }))
                        }
                        console.log(`maxId: ${maxId}, map.size: ${map.size}`)
                        resolve()
                    }).catch(err => reject(err))
                }

            }).on('error', err => {
                reject(err)
            })
        }).catch(err => {
            maxId = 0
            reject(err)
        })
    }
    resolve('all done')
})
let countdown = new Promise((resolve, reject) => {
    setTimeout(reject, 300000, 'time up');
})

async function save() {
    let data = []
    map.forEach(_ => {
        data.push(_)
    })
    data = data.sort((a, b) => Number(a.Id) > Number(b.Id) ? 1 : -1)
    data = data.map(_ => JSON.stringify(_) + '\n')
    await fs.writeFileSync('questions.txt', data)
    console.log(`${data.length} rows was inserted`)
}

Promise.race([countdown, action]).then(async value => {
    console.log(`crawler finished with ${value}`)
    await save()
}).catch(async err => {
    console.log(`crawler finished with ${err}`)
    await save()
})
