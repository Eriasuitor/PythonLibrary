const request = require('request')
const fs = require('fs')

async function done() {
    // let start = 0, size = 20
    // let writeStream = fs.createWriteStream('家有萌娃final.json')
    // let s = []
    // while (start < 9807) {
    //     request.get({
    //         url: `http://soogif.com/showimg?labelId=16&start=${start}&size=${size}`,
    //         headers: {
    //             // 'Accept': 'application/json'
    //         }
    //     }).on('data', data => {
    //         writeStream.write(data)
    //     })
    //     await new Promise(resolve => {
    //         setInterval(resolve, 3000)
    //     })
    //     writeStream.write(',\n')
    //     start += size
    //     console.log(start)
    // }
    // await writeStream.end()
    let labelIdList2 = [
        {
            id: 16,
            label: '家有萌娃'
        },
        {
            id: 35,
            label: '我真的不是神经病'
        },
        {
            id: 34,
            label: '尴尬瞬间'
        },
        {
            id: 33,
            label: '科技艺术'
        },
        {
            id: 32,
            label: '一般我不装'
        },
        {
            id: 31,
            label: '牛人炫技'
        },
        {
            id: 29,
            label: '美女动图'
        },
        {
            id: 28,
            label: '天下美食'
        },
        {
            id: 27,
            label: '综艺大咖'
        },
        {
            id: 25,
            label: '作死不要拉着我'
        },
        {
            id: 24,
            label: '整蛊专家'
        },
        {
            id: 23,
            label: '影视大赏'
        },
        {
            id: 22,
            label: '二次元世界'
        },
        {
            id: 30,
            label: '做人要有内涵'
        },
        {
            id: 37,
            label: '搞笑糗事'
        },
        {
            id: 17,
            label: '不懂脑回路'
        },
        {
            id: 26,
            label: '网红界扛把子'
        },
        {
            id: 19,
            label: '来啊斗图啊'
        },
        {
            id: 38,
            label: '惊险瞬间'
        },
        {
            id: 39,
            label: '帅哥'
        },
        {
            id: 40,
            label: '自然风景'
        },
        {
            id: 41,
            label: '体育集锦'
        },
        {
            id: 42,
            label: '军事'
        },
        {
            id: 43,
            label: '官方栏目'
        }, {
            id: 13,
            label: '萌物萌宠'
        }]
    let i = 0
    for (let labelId of labelIdList2) {
        i++
        let data = fs.readFileSync(`${labelId.label}_final.json`).toString()
        let resultList = []
        data.split(',\n').map(_ => {
            if (_) {
                if (_[_.length - 1] === ',')
                    _ = _.slice(0, _.length - 1)
                resultList = resultList.concat(JSON.parse(_).result.filter(a => a))
            }
        })
        let j = 0
        for (let item of resultList) {
            j++
            console.log(`[${i}/${labelIdList2.length}]${labelId.label} ${j}`)
            if (!fs.existsSync(labelId.label + (j >= 1000 ? Math.floor(j / 1000) : '')))
                fs.mkdirSync(labelId.label + (j >= 1000 ? Math.floor(j / 1000) : ''))
            console.log(labelId.label + (j >= 1000 ? Math.floor(j / 1000) : '') + '/' + item.gifurl.slice(item.gifurl.lastIndexOf('/') + 1, item.gifurl.length))
            if (fs.existsSync(labelId.label + (j >= 1000 ? Math.floor(j / 1000) : '') + '/' + item.gifurl.slice(item.gifurl.lastIndexOf('/') + 1, item.gifurl.length))) {
                console.log('存在')
                continue
            }
            await new Promise(async (resolve) => {

                // let writeStream = fs.createWriteStream(labelId.label + (j >= 1000 ? Math.floor(j / 1000) : '') + '/' + item.gifurl.slice(item.gifurl.lastIndexOf('/') + 1, item.gifurl.length))
                // writeStream.on('finish', () => {
                //     writeStream.end()
                //     resolve()
                // })
                let r = require('skip-request');
                let data = await r.get.url(item.gifurl).submit();
                data.toFile(labelId.label + (j >= 1000 ? Math.floor(j / 1000) : '') + '/' + item.gifurl.slice(item.gifurl.lastIndexOf('/') + 1, item.gifurl.length))

                return resolve();
                // request.get({
                //     url: item.gifurl
                // }).pipe(writeStream)
            })
            await new Promise(resolve => {
                setTimeout(resolve, 1000);
            })
        }
        // let start = 0, size = 20
        // while (true) {
        //     console.log(`[${i}/${labelIdList.length}]${labelId.label} ${start}`)
        //     await new Promise(resolve => {
        //         setTimeout(resolve, 3000);
        //     })
        //     let status = await new Promise(resolve => {
        //         request.get({
        //             url: `http://soogif.com/showimg?labelId=${labelId.id}&start=${start}&size=${size}`
        //         }, (error, resp, body) => {
        //             let data = JSON.parse(body)
        //             if (data.result.length === 0) resolve(1)
        //             writeStream.write(body + ',\n')
        //             resolve(0)
        //         })
        //     })
        //     if (status === 0) {
        //         start += size
        //         continue
        //     }
        //     writeStream.end()
        //     break
        // }
    }
}

done()

// let data = fs.readFileSync('萌物萌宠2.json')
// console.log((data.toString()).split('萌物萌宠').length)