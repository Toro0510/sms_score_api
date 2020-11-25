def classification_to_score(classification_result):
    if classification_result == '其他':
        return 0
    elif classification_result == '催收短信&信用卡套现':
        return 50
    elif classification_result == '还款提示':
        return 2
    elif classification_result == '扣还款成功&贷款信用卡分期申请成功':
        return -20
    elif classification_result == '扣还款失败&贷款信用卡分期申请失败':
        return 10
    elif classification_result == '交易支取短信':
        return -1
    elif classification_result == '贷款信用卡广告':
        return 1