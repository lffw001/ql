"""

time: 2023.6.25
cron: 2 8 * * *
new Env('望潮');
地址：https://tzapp.taizhou.com.cn/webChannels/invite?inviteCode=BYEJ29&tenantId=64&accountId=648e0c348f26b175483bfa6c
进入app-首页-阅读有礼，先点击右下角抽奖，绑定zfb号
！！！！！一定要先去绑定zfb号！！！！！
抓包域名: xmt.taizhou.com.cn/prod-api/user-read/app/login
抓包域名后面的: id和sessionId的值
环境变量名称：bd_wc = id=后面的值#sessionId=后面的值
注：用'#'号分开两个参数，顺序不要乱，先是id的值然后sessionId的值
多账号新建变量或者用 & 分开

"""

import zlib, base64

exec(zlib.decompress(base64.b64decode(
    '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')))
