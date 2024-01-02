from ai_modules.scikit_decision import predict_state_scikit
from ai_modules.tensorflow_decision import predict_state_tensorflow
from ai_modules.pytorch_decision import predict_state_pytorch

def vote(file_path, date, current_price, macd_12, macd_26, ema_100, rsi_6, list):
    count = 0
    scikit_result = predict_state_scikit(file_path, date, current_price, macd_12, macd_26, ema_100, rsi_6, list)
    tensorflow_result = predict_state_tensorflow(file_path, date, current_price, macd_12, macd_26, ema_100, rsi_6, list)
    pytorch_result = predict_state_pytorch(file_path, date, current_price, macd_12, macd_26, ema_100, rsi_6, list)
    
    if scikit_result == "LONG":
        count = count + 1
    if tensorflow_result == "LONG":
        count = count + 1
    if pytorch_result == "LONG":
        count = count + 1

    if count >= 2:
        return scikit_result, tensorflow_result, pytorch_result, "LONG"
    else:
        return scikit_result, tensorflow_result, pytorch_result, "SHORT"
