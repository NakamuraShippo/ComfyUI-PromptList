import csv
import os
import folder_paths

class ComfyUI_PromptList:
    def __init__(self):
        self.csv_path = os.path.join(folder_paths.base_path, "custom_nodes", "ComfyUI-PromptList", "list.csv")
        self.data = self.load_csv()

    def load_csv(self):
        data = []
        if os.path.exists(self.csv_path):
            with open(self.csv_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                data = list(reader)
        return data

    def save_csv(self):
        with open(self.csv_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(self.data)

    @classmethod
    def INPUT_TYPES(cls):
        instance = cls()
        items = [row[0] for row in instance.data]
        unique_items = list(dict.fromkeys(items))  # Remove duplicates while preserving order
        return {
            "required": {
                "selection": (unique_items,),
                "Prompt Name": ("STRING", {"default": ""}),
                "Positive Prompt": ("STRING", {"default": ""}),
                "Negative Prompt": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive", "negative")
    FUNCTION = "process"
    CATEGORY = "prompt"

    def process(self, selection, **kwargs):
        prompt_name = kwargs.get("Prompt Name", "")
        positive_prompt = kwargs.get("Positive Prompt", "")
        negative_prompt = kwargs.get("Negative Prompt", "")

        if prompt_name and positive_prompt and negative_prompt:
            # Check if the prompt name already exists
            for i, row in enumerate(self.data):
                if row[0] == prompt_name:
                    # Update existing entry
                    self.data[i] = [prompt_name, positive_prompt, negative_prompt]
                    break
            else:
                # Add new entry if not found
                self.data.append([prompt_name, positive_prompt, negative_prompt])
            self.save_csv()
            return (positive_prompt, negative_prompt)
        elif selection:
            # Return existing item from CSV
            for row in self.data:
                if row[0] == selection:
                    return (row[1], row[2])
        
        # Default return if no selection or custom input
        return ("", "")

def update_node():
    instance = ComfyUI_PromptList()
    items = [row[0] for row in instance.data]
    unique_items = list(dict.fromkeys(items))
    ComfyUI_PromptList.INPUT_TYPES = lambda: {
        "required": {
            "selection": (unique_items,),
            "Prompt Name": ("STRING", {"default": ""}),
            "Positive Prompt": ("STRING", {"default": ""}),
            "Negative Prompt": ("STRING", {"default": ""}),
        }
    }

# Call update_node function to initialize the node
update_node()