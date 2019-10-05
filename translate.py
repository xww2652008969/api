import execjs
import requests
import json
he['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
js='''
function vq(a,uq='436121.1791969162') {
    if (null !== uq)
        var b = uq;
    else {
        b = sq('T');
        var c = sq('K');
        b = [b(), c()];
        b = (uq = window[b.join(c())] || "") || ""
    }
    var d = sq('t');
    c = sq('k');
    d = [d(), c()];
    c = "&" + d.join("") + "=";
    d = b.split(".");
    b = Number(d[0]) || 0;
    for (var e = [], f = 0, g = 0; g < a.length; g++) {
        var l = a.charCodeAt(g);
        128 > l ? e[f++] = l : (2048 > l ? e[f++] = l >> 6 | 192 : (55296 == (l & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (l = 65536 + ((l & 1023) << 10) + (a.charCodeAt(++g) & 1023),
        e[f++] = l >> 18 | 240,
        e[f++] = l >> 12 & 63 | 128) : e[f++] = l >> 12 | 224,
        e[f++] = l >> 6 & 63 | 128),
        e[f++] = l & 63 | 128)
    }
    a = b;
    for (f = 0; f < e.length; f++)
        a += e[f],
        a = tq(a, "+-a^+6");
    a = tq(a, "+-3^+b+-f");
    a ^= Number(d[1]) || 0;
    0 > a && (a = (a & 2147483647) + 2147483648);
    a %= 1000000;
    return(a.toString() + "." + (a ^ b))
};
 
/*--------------------------------------------------------------------------------
参数：a 为你要翻译的原文
其他外部函数：
--------------------------------------------------------------------------------*/
function sq(a) {
    return function() {
        return a
    }
}
 
function tq(a, b) {
    for (var c = 0; c < b.length - 2; c += 3) {
        var d = b.charAt(c + 2);
        d = "a" <= d ? d.charCodeAt(0) - 87 : Number(d);
        d = "+" == b.charAt(c + 1) ? a >>> d : a << d;
        a = "+" == b.charAt(c) ? a + d & 4294967295 : a ^ d
    }
    return a
}
'''
a=execjs.compile(js)
def translate(q，a,b):  #a为输入语言 b为翻译目标语言 返回
    data={}
    data['client']='webapp'
    data['sl']=a
    data['tl']=b
    data['hl']='zh-CN'
    data['dt']='at'
    data['tk']=a.call('vq',q)
    data['q']=q
    url='https://translate.google.cn/translate_a/single'
    try:
        text=requests.get(url,params=data,headers=he)
        aa=json.loads(text.text)
        return aa[5][0][2][0][0]
    except:
        return 0
