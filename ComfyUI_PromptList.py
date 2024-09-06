import yaml
import os
import folder_paths
from collections import OrderedDict

# カスタムYAMLローダーとダンパーを定義
class OrderedLoader(yaml.SafeLoader):
    pass

class OrderedDumper(yaml.SafeDumper):
    pass

def dict_constructor(loader, node):
    return OrderedDict(loader.construct_pairs(node))

OrderedLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, dict_constructor)

def dict_representer(dumper, data):
    return dumper.represent_mapping(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, data.items())

OrderedDumper.add_representer(OrderedDict, dict_representer)

class ComfyUI_PromptList:
    def __init__(self):
        self.yaml_path = os.path.join(folder_paths.base_path, "custom_nodes", "ComfyUI-PromptList", "prompts.yaml")
        self.data = self.load_yaml()

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "selection": (cls.get_prompt_list(),),
                "Prompt Name": ("STRING", {"multiline": True}),
                "Positive Prompt": ("STRING", {"multiline": True}),
                "Negative Prompt": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive", "negative")
    FUNCTION = "process"
    CATEGORY = "prompt"

    def load_yaml(self):
        if os.path.exists(self.yaml_path):
            with open(self.yaml_path, 'r', encoding='utf-8') as file:
                return yaml.load(file, Loader=OrderedLoader) or OrderedDict()
        return OrderedDict()

    def save_yaml(self):
        with open(self.yaml_path, 'w', encoding='utf-8') as file:
            yaml.dump(self.data, file, Dumper=OrderedDumper, allow_unicode=True)

    @classmethod
    def get_prompt_list(cls):
        instance = cls()
        return list(instance.data.keys())

    def process(self, selection, **kwargs):
        prompt_name = kwargs.get("Prompt Name", "")
        positive_prompt = kwargs.get("Positive Prompt", "")
        negative_prompt = kwargs.get("Negative Prompt", "")

        if prompt_name:
            # プロンプト名が入力されている場合の処理
            if prompt_name in self.data:
                # 既存のプロンプトを更新
                if positive_prompt:
                    self.data[prompt_name]["positive"] = positive_prompt
                if negative_prompt:
                    self.data[prompt_name]["negative"] = negative_prompt
            else:
                # 新しいプロンプトを作成
                self.data[prompt_name] = OrderedDict([
                    ("positive", positive_prompt or ""),
                    ("negative", negative_prompt or "")
                ])
            self.save_yaml()
            return (self.data[prompt_name]["positive"], self.data[prompt_name]["negative"])
        elif selection:
            # 既存のプロンプトを選択した場合の処理
            prompt = self.data.get(selection, {})
            return (prompt.get("positive", ""), prompt.get("negative", ""))
        
        # デフォルトの戻り値（何も選択されず、新規入力もない場合）
        return ("", "")

    @classmethod
    def IS_CHANGED(cls, *args, **kwargs):
        return float("NaN")

# NODE_CLASS_MAPPINGS と NODE_DISPLAY_NAME_MAPPINGS の定義
NODE_CLASS_MAPPINGS = {
    "ComfyUI-PromptList": ComfyUI_PromptList
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI-PromptList": "Prompt List"
}