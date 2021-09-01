from msg_queue.tasks import inference


def controller_inference(json_data):
    result = inference.delay(json_data)
    return result
