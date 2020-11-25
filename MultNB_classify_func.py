import joblib
import json
import pandas as pd
import sms_filter
import useful_word
import cal_score


def load_json_str(file):
    with open(file, 'r', encoding="utf-8") as f:
        json_str = json.loads(f.read())
        return json_str


# def dict_slice(ori_dict, start, end):
#     """
#     字典类切片
#     :param ori_dict: 字典
#     :param start: 起始
#     :param end: 终点
#     :return:
#     """
#     slice_dict = {k: ori_dict[k] for k in list(ori_dict.keys())[start:end]}
#     return slice_dict


def predict_socre(sms_list):
    clf = joblib.load('MultinomialNB.pkl')
    # 读取模型文件

    json_df = pd.DataFrame(sms_list, columns=['body'])
    # 生成Dataframe

    json_df['sms_filter'] = json_df['body'].apply(lambda x: sms_filter.sms_filter_func(str(x)))
    json_df = json_df[(json_df['sms_filter'] == True)]
    json_df.reset_index()
    # 筛选有效短信

    if len(json_df) == 0:
        total_score = 0

    else:
        for i in useful_word.useful_word:
            json_df[i] = json_df['body'].apply(lambda x: useful_word.word_regexp(i, x))
        # 生成哑变量

        model_data = json_df.iloc[:, -len(useful_word.useful_word):]
        json_df['predict_result'] = clf.predict(model_data)
        # 预测短信分类

        json_df['score'] = json_df['predict_result'].apply(lambda x: cal_score.classification_to_score(x))
        total_score = sum(json_df['score'])
        # 汇总评分

    return total_score


if __name__ == '__main__':
    with open('json_str.txt', 'r', encoding="utf-8") as f:
        json_str = json.loads(f.read())
