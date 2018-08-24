const request = require('request')
const fs = require('fs')

let result = []
let map = new Map()
let finished = false

function finish() {
    map.forEach(_ => result.push(_))
    fs.writeFileSync('zaml2018.json', result.map(_ => JSON.stringify(_) + '\n'))
}

let action = new Promise(async resolve => {
    let i = 0
    while (i < 360) {
        await new Promise(resolve => {
            request.post({
                url: 'https://pinyin.zaml2018.com/pyjyz/api/v1_0_5/challenge/start',
                "headers": {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Cache-Control": "no-cache",
                },
                body: "user_id=164189&timestamp=1534830186685&sign=501a10bbed32ccc9e1a4eb8f6c9ca815"
            }, function (error, response, body) {
                if (error) reject(error);
                let data = JSON.parse(body)
                for (let d of data.data.words) {
                    map.set(d.primary, d)
                }
                resolve()
            })
        }).catch(error => {
            console.log(error)
        })
        console.log(map.size)
        if(finished) console.log('time out')
        i++
        await new Promise(resolve => {
            setTimeout(resolve, 1000)
        })
    }
    resolve('finished')
})


let counter = new Promise((resolve, reject) => {
    setTimeout(resolve, 420000, 'time out')
})

Promise.race([action, counter]).then(value => {
    console.log(value)
    finish()
}).catch(error => {
    console.log(error)
    finished = true
    finish()
})

    // let i = 1
    // while (i <= 17) {
    //     let writeStream = fs.createWriteStream(`level/nor_${i}.png`)
    //     let writeStream2 = fs.createWriteStream(`level/sel_${i}.png`)
    //     await new Promise(resolve => {
    //         writeStream.on('finish', () => {
    //             console.log(2)

    //             writeStream2.on('finish', () => {
    //                 console.log(1)
    //                 i++
    //                 resolve()
    //             })
    //             request.get({ url: `http://xcxcy.oss-cn-hangzhou.aliyuncs.com/cycck/level/sel_${i}.png` }).pipe(writeStream2)
    //         })
    //         request.get({ url: `http://xcxcy.oss-cn-hangzhou.aliyuncs.com/cycck/level/nor_${i}.png` }).pipe(writeStream)
    //     })
    // }




// var qs = require("querystring");
// var http = require("https");

// var options = {
//     "method": "POST",
//     "hostname": 'pinyin.zaml2018.com',
//     "path": "/pyjyz/api/v1_0_5/challenge/start",
//     "headers": {
//         "Content-Type": "application/x-www-form-urlencoded",
//         "Cache-Control": "no-cache",
//     }
// };

// var req = http.request(options, function (res) {
//     var chunks = [];

//     res.on("data", function (chunk) {
//         chunks.push(chunk);
//     });

//     res.on("end", function () {
//         var body = Buffer.concat(chunks);
//         console.log(body.toString());
//     });
// });

// req.write(qs.stringify({
//     user_id: '164189',
//     timestamp: '1534830186685',
//     sign: '501a10bbed32ccc9e1a4eb8f6c9ca815'
// }));
// console.log(qs.stringify({
//     user_id: '164189',
//     timestamp: '1534830186685',
//     sign: '501a10bbed32ccc9e1a4eb8f6c9ca815'
// }))
// req.end();