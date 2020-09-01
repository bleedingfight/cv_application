import pytest
import cores.models_info_pb2 as models_info_pb2
@pytest.mark.read_config
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
# def test():
#     assert 1==2
def check_model():
    obj = models_info_pb2.modelInfo()
    obj.model_name = "resnet.pb"
    obj.model_config = "config.pbtxt"
    obj.model_label = "labels.txt"
    with open('test.pbtxt','wb') as f:
        flag = f.write(obj.SerializeToString())
    assert flag == True

@pytest.mark.write_config
def check_model():
    pass
if __name__ == "__main__":
    pytest.main(['-v','start_model_test.py','-m=read_config'])