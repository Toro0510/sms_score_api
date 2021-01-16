import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import MultNB_classify_func
import logging
import time


class Item(BaseModel):
    order_number: str
    sms: list


logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                    filename='logging.txt',
                    filemode='w',
                    # 模式，有W和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    # 日志格式
                    )

app = FastAPI()


@app.get("/")
async def get_info():
    '''
    短信评分接口
    '''
    msg = '短信评分接口'
    return msg


# @app.post("/upload/")
# async def postUploadFileApi(file: UploadFile = File(None)):
#     '''
#     返回结果
#     details：返回每条有效短信预测分类结果及得分
#     total_score：当前订单短信汇总评分
#     '''
#     contents = await file.read()
#     contents = str(contents, encoding="utf-8")
#     json_str = eval(contents)
#     result = MultNB_classify_func.predict_socre(json_str)
#
#     with open('score_result.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
#         file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ': ' + result + "\n")
#
#     return result


@app.post("/json_str/")
async def sms_score_predict(item: Item):
    '''
    返回结果
    details：返回每条有效短信预测分类结果及得分
    total_score：当前订单短信汇总评分
    '''

    result_dict = {}
    score_result = str(MultNB_classify_func.predict_socre(item.sms))
    result_dict['order_number'] = item.order_number
    result_dict['total_score'] = score_result

    with open('score_result.txt', "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
        file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ': ' + str(result_dict) + "\n")

    json_response_data = jsonable_encoder(result_dict)
    return JSONResponse(content=json_response_data)


if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8000)
    # uvicorn.run(app=app, host='0.0.0.0', port=8080)
