def sms_filter_func(str):
    sms_filter_word = [
        '验证码',
        '校验码',
        '激活码',
        '联通',
        '电信',
        '移动',
        '充值',
        '话费',
        '积分',
        '套餐',
        '流量',
        '天猫',
        '淘宝',
        '拼多多',
        '腾讯',
        '商城',
        '快件',
        'EMS',
        '外卖',
        '送餐',
        '美团',
        '饿了么'
        '58同城',
        'BOSS直聘',
        '滴滴',
        '包裹',
        '快递',
        '12306',
        '10086',
        '航班',
        '旗舰',
        '面试',
        '薪资',
        '消防',
        '救援',
        '防空',
        '国家',
        '扶贫',
        '食品',
        '人口',
        '教育',
        '医疗',
        '扫黑',
        '旅游',
        '打车',
        '旅客',
        '福利',
        '红包',
        '出租',
        '房源',
        '链接',
        '会员',
        '活动',
        '优惠',
        '满意',
        '元宝',
        '专营',
        '温馨',
        '免费',
        'KTV',
        'luckin coffee',
        '抖音',
        '快手',
        '探探',
        '脉脉',
        '防疫',
        '疫情',
        '物业',
        '公益',
        '简历',
        '抢票',
        '车票',
        '机票',
        '火车',
        '酒店',
        '旅行',
        '电力',
        '交警',
        '体检',
        '音乐',
        '招聘',
        '好友',
        '双11',
        '骑行易',
        '哈啰',
        '买菜',
        '唯品会',
        '农业',
        '自然资源',
        '藏宝阁',
        '森林',
        '税务',
        '拼车',
        '水利',
        '复工',
        '复产',
        '文明',
        '预警',
        '酒驾',
        '醉驾',
        '家长',
        '作业',
        '老师',
        '教师',
        '洗衣机',
        '开盘',
        '运费'
    ]
    for i in sms_filter_word:
        if i in str or len(str) < 25:
            return False
    else:
        return True
