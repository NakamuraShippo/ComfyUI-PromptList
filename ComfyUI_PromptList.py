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
        self.user_folder = os.path.join(folder_paths.base_path, "user")
        self.prompt_list_folder = os.path.join(self.user_folder, "PromptList")
        self.yaml_path = os.path.join(self.prompt_list_folder, "prompts.yaml")
        self.ensure_yaml_file_exists()
        self.data = self.load_yaml()

    def ensure_yaml_file_exists(self):
        if not os.path.exists(self.prompt_list_folder):
            os.makedirs(self.prompt_list_folder, exist_ok=True)
        if not os.path.exists(self.yaml_path):
            with open(self.yaml_path, 'w', encoding='utf-8') as file:
                yaml.dump({}, file, Dumper=OrderedDumper)

    def load_yaml(self):
        with open(self.yaml_path, 'r', encoding='utf-8') as file:
            return yaml.load(file, Loader=OrderedLoader) or OrderedDict()

    def save_yaml(self):
        with open(self.yaml_path, 'w', encoding='utf-8') as file:
            yaml.dump(self.data, file, Dumper=OrderedDumper, allow_unicode=True)

    @classmethod
    def INPUT_TYPES(cls):
        instance = cls()
        items = list(instance.data.keys())
        # デフォルトの選択肢を追加
        items = ["input as prompt name"] + items
        return {
            "required": {
                "selection": (items,),
                "Prompt Name": ("STRING", {"default": ""}),
                "Positive Prompt": ("STRING", {"default": ""}),
                "Negative Prompt": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive", "negative")
    FUNCTION = "process"
    CATEGORY = "prompt"

    @classmethod
    def get_prompt_list(cls):
        instance = cls()
        return list(instance.data.keys())

    def process(self, selection, **kwargs):
        prompt_name = kwargs.get("Prompt Name", "")
        positive_prompt = kwargs.get("Positive Prompt", "")
        negative_prompt = kwargs.get("Negative Prompt", "")

        if selection == "input as prompt name":
            # 新しいプロンプト名として扱う
            prompt_name = prompt_name or selection

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
        elif selection and selection != "input as prompt name":
            # 既存のプロンプトを選択した場合の処理
            prompt = self.data.get(selection, {})
            return (prompt.get("positive", ""), prompt.get("negative", ""))
        
        # デフォルトの戻り値（何も選択されず、新規入力もない場合）
        return ("", "")

    @classmethod
    def IS_CHANGED(cls, *args, **kwargs):
        return float("NaN")

NODE_CLASS_MAPPINGS = {
    "ComfyUI-PromptList": ComfyUI_PromptList
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI-PromptList": "Prompt List"
}