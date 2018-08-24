const request = require('request')
const fs = require('fs')

new Promise(resolve => {
    request.get({url: 'https://hanyu.baidu.com/s?wd=%E4%BB%80%E4%B9%88&from=zici'}, (error, response, body) => {
        console.log(body)
        resolve()
    })
})