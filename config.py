#当前请求次数
REQUEST_NUM = 0

#请求多少次后换IP配置
CHANGE_IP = 0

#代理IP
IP = ''

#
# executable_path = '/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs'

START_URL = 'https://m.baidu.com/s?tn=zbios&bd_page_type=1&word={kw}'

#是否开启代理
PROXY_SWITCH = False
#是否使用cookies
COOKIES_SWITCH = False
#请求最大出错次数
ERROR_MAX = 3

#请求头配置
HEADERS = {
    'connection': "keep-alive",
    'cache-control': "max-age=0",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # 'cookie': 'BAIDUID=5D8A2804B938E146094FE12FE635B220:FG=1; BDUSS=WZMUWd5NDluanBZcXZBWmlxV2pkc2kxcWEtUUpZcUZuLU1UMTdpMUN5RmhpT1piQVFBQUFBJCQAAAAAAAAAAAEAAAAVrzREZGZpdDQxOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGH7vlth-75bY; PSTM=1539319605; BIDUPSID=DCAE3195BFEA154D50EA26B9F9412D65; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; FEED_SIDS=823024_1025_10; plus_lsv=fca6ea75f81978a4; plus_cv=1::m:d03af37f; BDICON=10123156; ysm=9093|10223; PSINO=6; H_WISE_SIDS=100459; MSA_PBT=0; H_PS_PSSID=1432_21098_27400_20719; BDPASSGATE=IlPT2AEptyoA_yiU4VO83kIN8efjVvGAAfeGSDRtRlO4fCaWmhH33bVMSEnHN-a8AiTM-YyfmqxtpjrFV6xjg0N_gRsTkTZug6zd7Nif5avvH1tA-rdo_bX5UCUOm3PHh4JL-3MEF3VCZEkCpubxgewmcOqsxQNvecLItULomMrs1TCG1Xrvx9KuK9p5YnjYN0_Xx3jEhShwKSmBUuL2HDTLpCQhP8wtx2O9atE-AOv-vj1LHe0dOPMe1_; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695; MSA_WH=612_900; MSA_ZOOM=1056; lsv=zbiosTjs_78e7170-zbiosTcss_92f145a-zbiosBcss_85ae3ae-footjs_2b01201-ios_invokeAppjs_07e1aa6-globalBjs_a9421b5-sugjs_3ac2fc6-zbiosjs_472aeca-framejs_504ce6b; BDSVRBFE=Go; wise_tj_cl=i@0|v@1|sInfo@1920_1080_1920_1057_1831_900|fInfo@23_0_20_23|dpr@1; wpr=0; __bsi=9994125698870235864_h2_22_N_R_3_0303_c02f_Y'
}

js_str = '''
    getParam = function(t) {
        var n = function() {
            for (var t = 0, e = new Array(256), n = 0; 256 !== n; ++n)
                t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = 1 & (t = n) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1) ? -306674912 ^ t >>> 1 : t >>> 1,
                e[n] = t;
            return "undefined" != typeof Int32Array ? new Int32Array(e) : e
        }();
        for (var e, r, i = -1, o = 0, a = t.length; o < a; )
            (e = t.charCodeAt(o++)) < 128 ? i = i >>> 8 ^ n[255 & (i ^ e)] : e < 2048 ? i = (i = i >>> 8 ^ n[255 & (i ^ (192 | e >> 6 & 31))]) >>> 8 ^ n[255 & (i ^ (128 | 63 & e))] : e >= 55296 && e < 57344 ? (e = 64 + (1023 & e),
            r = 1023 & t.charCodeAt(o++),
            i = (i = (i = (i = i >>> 8 ^ n[255 & (i ^ (240 | e >> 8 & 7))]) >>> 8 ^ n[255 & (i ^ (128 | e >> 2 & 63))]) >>> 8 ^ n[255 & (i ^ (128 | r >> 6 & 15 | (3 & e) << 4))]) >>> 8 ^ n[255 & (i ^ (128 | 63 & r))]) : i = (i = (i = i >>> 8 ^ n[255 & (i ^ (224 | e >> 12 & 15))]) >>> 8 ^ n[255 & (i ^ (128 | e >> 6 & 63))]) >>> 8 ^ n[255 & (i ^ (128 | 63 & e))];
        return (-1 ^ i) >>> 0
    };
'''