const fs = require('fs')

async function done() {
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
        let data = fs.readFileSync(`../${labelId.label}_final.json`).toString()
        let resultList = []
        data.split(',\n').map(_ => {
            if (_) {
                if (_[_.length - 1] === ',')
                    _ = _.slice(0, _.length - 1)
                resultList = resultList.concat(JSON.parse(_).result.filter(a => a))
            }
        })
        fs.writeFileSync(`${labelId.label}.json`, resultList.map(_ => JSON.stringify(_) + '\n'))
    }
}

done()

// let data = fs.readFileSync('萌物萌宠2.json')
// console.log((data.toString()).split('萌物萌宠').length)