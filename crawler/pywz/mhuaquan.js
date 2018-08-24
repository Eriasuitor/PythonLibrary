const request = require('request')
const fs = require('fs')

let map = new Map()

fs.readFileSync('mhuaquan.json').toString().split('\n,').map(_ => {
    _ = JSON.parse(_)
    map.set(_.ID, _)
})

let getOne =() =>  new Promise((resolve, reject) => {
    request.post({
        url: 'https://pinyin.xcx01.mhuaquan.com/v1/wx/StartFreePlay',
        headers:
        {
            'content-type': 'application/json'
        },
        body: JSON.stringify({ userId: '2EsqXLQecOv9UrHj1usSpQqM4OFWtLQFY746SAXoVv8=' })
    }, (error, response, body) => {
        if (error) reject(error)
        JSON.parse(JSON.parse(body).DataObj.StrTiku).map(_ => {
            map.set(_.ID, _)
        })
        console.log(map.size)
        resolve()
    })
})

let action = new Promise(async resolve => {
    for (let i = 0; i < 360; i++) {
        await getOne().catch(error => {
            reject(error)
        })
        await new Promise(resolve => {
            setTimeout(resolve, 1000, 'wait');
        })
    }
    resolve('finished')
})

let counter = new Promise((resolve, reject) => {
    setTimeout(reject, 750000, 'time up');
})

let save = () => {
    let result = []
    map.forEach(_ => result.push(_))
    fs.writeFileSync('mhuaquan.json', result.map(_ => JSON.stringify(_) + '\n'))
}

Promise.race([action, counter]).then(value => {
    console.log(value)
    save()
}).catch(error => {
    console.log(error)
    save()
})