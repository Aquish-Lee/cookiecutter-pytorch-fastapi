import json
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from controller.model_controller import controller_inference


class Data_form(BaseModel):
    img_string: Optional[str] = Field(
            default="",
            description="string format image encoded with base64")


app = FastAPI(
    title="{{cookiecutter.project_name}}",
    version="1.0",
    description="{{cookiecutter.project_short_description}}"
)


@app.post("/inference")
async def inference(data: Data_form):
    ret_value = None

    if not data:
        return JSONResponse(status_code=401, content={'task_id': None, 'result': ret_value, 'msg': '未得到数据'})

    send_data = {
        "img_string": data.img_string
}
    task = controller_inference(json.dumps(send_data))

    if not task:
        return JSONResponse(status_code=402, content={'task_id': None, 'result': ret_value, 'msg': '接口内部错误'})

    ret_value = task.get()[1:-1]
    return JSONResponse(status_code=200, content={'task_id': str(task.id), 'result': ret_value, 'msg': '请求成功'})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fastapi_app:app", host="0.0.0.0", port=5000, workers=1)
