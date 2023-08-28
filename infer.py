import torch
from modelscope import Model, snapshot_download
from modelscope.models.nlp.llama2 import Llama2Tokenizer


model_dir = snapshot_download("modelscope/Llama-2-13b-chat-ms", cache_dir="../model_cache", revision='v1.0.2', 
                              ignore_file_pattern=[r'.+\.bin$'])
tokenizer = Llama2Tokenizer.from_pretrained(model_dir)
model = Model.from_pretrained(
    model_dir,
    torch_dtype=torch.float16,
    device_map='auto')

system = 'you are a helpful assistant in ai transformer and attention mechanism!'
inputs = {'text': 'Tell me details about how to design a visual transformer Architecture?', 'system': system, 'max_length': 2048}
output = model.chat(inputs, tokenizer)
print(output['response'])

inputs = {'text': 'What places can we learn more?', 
          'system': system, 
          'history': output['history'],
          'max_length': 2048}
output = model.chat(inputs, tokenizer)
print(output['response'])
