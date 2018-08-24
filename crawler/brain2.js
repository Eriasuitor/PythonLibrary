var request = require("request");

var options = { method: 'POST',
  url: 'https://cpy.dundashi.com.cn/api/v1/startgame',
  headers: 
   {
     'content-type': 'application/json'
     },
  body: '{ "openid": "TWpNek1USmpZM2x4YzNOTVkwcE1NV3c0YW01c1EyTjU" }),
};

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});


//curl 'https://csdnimg.cn/public/sandalstrap/1.3/css/sandalstrap.min.css' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' --compressed -H 'Connection: keep-alive'