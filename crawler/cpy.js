let http = require("https");
const fs = require('fs')

let dataOld = fs.readFileSync('cpyData.txt').toString()
dataOld = dataOld.split('\n,').map(_ => JSON.parse(_))
let map = new Map()
dataOld.map(_ => {
  if (_ && _.list)
    map.set(_.list[0] + _.list[1], _)
})

let options = {
  "method": "POST",
  "hostname": 'cpy.dundashi.com.cn',
  "path": '/api/v1/startgame',
  "headers": {
    "Content-Type": "application/json",
  }
};

new Promise(async resolve => {
  for (let i = 0; i < 100; i++) {
    await new Promise(resolve => {
      let req = http.request(options, function (res) {
        let chunks = [];

        res.on("data", function (chunk) {
          chunks.push(chunk);
        });

        res.on("end", function () {
          let body = Buffer.concat(chunks);
          let data = JSON.parse(body.toString()).sub_data;
          console.log(data)
          data.map(_ => {
            if (_ && _.list)
              map.set(_.list[0] + _.list[1], _)
          })
          resolve()
        });
      });
      req.write(JSON.stringify({ openid: 'TWpNek1USmpZM2x4YzNOTVkwcE1NV3c0YW01c1EyTjU' }));
      req.end();
    })
  }
  resolve()
}).then(() => {
  let data = []
  map.forEach(_ => {
    data.push(_)
  })
  data = data.map(_ => JSON.stringify(_) + '\n')
  fs.writeFileSync('cpyData.txt', data)
  console.log(`${data.length} rows was inserted`)
})
