# -*- coding: utf-8 -*-
# @Author  : Aquish
# @Organization : NTT
import json
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from controller.model_controller import controller_inference


class data_form(BaseModel):
    img_string: Optional[str] = Field(
            default="",
            description="string format image encoded by base64")


app = FastAPI(
    title="{{cookiecutter.project_name}}",
    version="1.0",
    description="{{cookiecutter.project_short_description}}"
)


@app.post("/inference")
async def inference(data: data_form):

    if not data:
        return JSONResponse(status_code=401, content={'task_id': None, 'result': None, 'msg': '未得到数据'})

    send_data = {
        "img_string": data.img_string
}
    task = controller_inference(json.dumps(send_data))

    if not task:
        return JSONResponse(status_code=402, content={'task_id': None, 'result': None, 'msg': '接口内部错误'})

    return JSONResponse(status_code=200, content={'task_id': str(task.id), 'result': json.loads(task.get()), 'msg': '请求成功'})
