def word_regexp(i, x):
    if i in x:
        return 1
    else:
        return 0


useful_word = [
    '还款',
    '银行',
    '尾号',
    '支付',
    '信用',
    '余额',
    '人民',
    '账户',
    '人民币',
    '信用卡',
    '支付宝',
    '账单',
    '退订',
    '尊敬',
    '中国',
    '申请',
    '金额',
    '金融',
    '商银',
    '逾期',
    '交易',
    '忽略',
    '额度',
    '客户',
    '公司',
    '农业',
    '完成',
    '农业银行',
    '消费',
    '分期',
    '贷款',
    '借款',
    '快捷',
    '服务',
    '还款日',
    '我行',
    '点击',
    '扣款',
    '登录',
    '信息',
    '先生',
    '有限',
    '回复',
    '成功',
    '有限公司',
    '失败',
    '如已还款',
    '自动',
    '本期',
    '影响',
    '联系',
    '支出',
    '如有',
    '通过',
    '个人',
    '款额',
    '疑问',
    '提醒',
    '最低',
    '工商',
    '管理',
    '查看',
    '使用',
    '平安',
    '储蓄',
    '办理',
    '储蓄卡',
    '最低还款',
    '电话',
    '还款额',
    '进行',
    '自动还款',
    '到期',
    '记录',
    '欠款',
    '查询',
    '征信',
    '客服',
    '处理',
    '银行卡',
    '招商',
    '个人信用',
    '尽快',
    '及时',
    '银行信用',
    '兴业',
    '公众',
    '最高',
    '手机',
    '建设',
    '您好',
    '避免',
    '疑问请',
    '咨询',
    '中信',
    '短信',
    '已逾期',
    '用户',
    '剩余',
    '查账',
    '过期',
    '更多',
    '转账',
    '小时',
    '致电',
    '网络',
    '生活',
    '通知',
    '账号',
    '应还金额',
    '收入',
    '立即',
    '马上',
    '女士',
    '不足',
    '可用',
    '时间',
    '续费',
    '未还',
    '系统',
    '邮储',
    '根据',
    '安全',
    '今日',
    '详情',
    '可能',
    '为准',
    '还清',
    '当前',
    '最后',
    '活期',
    '日前',
    '业务',
    '手续',
    '工作',
    '规定',
    '手续费',
    '备用',
    '保证',
    '备用金',
    '感谢',
    '浦发',
    '有效',
    '科技',
    '理会',
    '交通',
    '领取',
    '款项',
    '开通',
    '提现',
    '审核',
    '确保',
    '操作',
    '下载',
    '报送',
    '蚂蚁',
    '借条',
    '诈骗',
    '充足',
    '关注',
    '基金',
    '网上',
    '确认',
    '已经',
    '已成',
    '催收',
    '还款失败',
    '要求',
    '应急',
    '财物',
    '今天',
    '中心',
    '资金',
    '核对',
    '拨打',
    '发生',
    '可以',
    '提供',
    '扣款失败',
    '人员',
    '最后还款日',
    '提示',
    '民生',
    '严重',
    '感谢您',
    '其他',
    '再次',
    '渠道',
    '平台',
    '不良',
    '谨防',
    '存入',
    '合同',
    '归还',
    '多次',
    '数据',
    '基础',
    '拍拍',
    '钱包',
    '借记',
    '产品',
    '请于',
    '借记卡',
    '正常',
    '相关',
    '情况',
    '打开',
    '本次',
    '多服',
    '请勿',
    '拖欠',
    '助理',
    '数据库',
    '据库',
    '现金',
    '投资',
    '产生',
    '即可',
    '光大',
    '资格',
    '激活',
    '热线',
    '为了',
    '订单',
    '条例',
    '云南',
    '本人',
    '直接',
    '行将',
    '行为',
    '结果',
    '无法',
    '约定',
    '管理条例',
    '足额',
    '截止',
    '注意',
    '利率',
    '卡号',
    '转存',
    '理财',
    '提醒您',
    '自行',
    '违约',
    '身份',
    '责任',
    '卡片',
    '付款',
    '进入',
    '签约',
    '入账',
    '核实',
    '按时',
    '原因',
    '由于',
    '每期',
    '在线',
    '单号',
    '否则',
    '选择',
    '偿还',
    '无需',
    '提交',
    '了解',
    '工作人员',
    '作人',
    '实际',
    '管理厅',
    '您提',
    '已还清',
    '本月',
    '本金',
    '退款',
    '快速',
    '审批',
    '代扣',
    '上报',
    '借钱',
    '法院',
    '密码',
    '已过',
    '问题',
    '造成',
    '继续',
    '支持',
    '生银',
    '截至',
    '身份证',
    '绑定',
    '强制',
    '法律',
    '以免',
    '受骗',
    '良好',
    '购物',
    '亲爱',
    '四川',
    '已为',
    '抱歉',
    '公示',
    '人民银行',
    '单人',
    '前往',
    '更新',
    '放款',
    '失效',
    '当天',
    '掌上',
    '集团',
    '你好',
    '发送',
    '名单',
    '通道',
    '全额',
    '获得',
    '权益',
    '司法',
    '执行',
    '全球',
    '黄河',
    '接交',
    '交予',
    '收工',
    '至少',
    '网上支付',
    '方式',
    '买单',
    '来电',
    '尝试',
    '国人',
    '自助',
    '配合',
    '推荐',
    '保险',
    '分子',
    '一笔',
    '珍惜',
    '程序',
    '搜索',
    '联系电话',
    '付交',
    '开始',
    '不法',
    '体验',
    '信贷',
    '实施',
    '北京',
    '证件',
    '不法分子',
    '地址',
    '一步',
    '资料',
    '恢复',
    '总额',
    '天将',
    '发信',
    '认证',
    '一期',
    '转入',
    '结清',
    '代付',
    '风险',
    '祝您',
    '游戏',
    '随时',
    '作废',
    '协商',
    '如实',
    '任何',
    '商户',
    '冷静',
    '分钟',
    '即将',
    '对方',
    '号码',
    '生效',
    '手机号',
    '技术',
    '诉讼',
    '银行账',
    '交友',
    '兼职',
    '机构',
    '提升',
    '进一步',
    '现在',
    '保障',
    '轻信',
    '代办',
    '计算',
    '赌博',
    '银联',
    '卡内',
    '还有',
    '失信',
    '转出',
    '可为',
    '支取',
    '修改',
    '计划',
    '请拨',
    '不能',
    '措施',
    '退回',
    '保单',
    '分别',
    '违约金',
    '接听',
    '重新',
    '未通',
    '收到',
    '大家',
    '欢迎',
    '因为',
    '恶意',
    '提前',
    '采取',
    '以上',
    '统计',
    '愉快',
    '评估',
    '维护',
    '全部',
    '深圳',
    '详情请',
    '没有',
    '主动',
    '效期',
    '现已',
    '履行',
    '非本',
    '有效期',
    '社会',
    '后续',
    '不要',
    '存款',
    '成都',
    '未接',
    '如果',
    '预计',
    '首付',
    '届时',
    '告知',
    '归属',
    '还款支付宝',
    '收款',
    '央行',
    '户籍',
    '回电',
    '付息',
    '设置',
    '过期作废',
    '户名',
    '快来',
    '自己',
    '已于',
    '芝麻',
    '企业',
    '公安',
    '同城',
    '健康',
    '依法',
    '特权',
    '送至',
    '消息',
    '确保您',
    '主叫',
    '生好',
    '防护',
    '取消'
]
