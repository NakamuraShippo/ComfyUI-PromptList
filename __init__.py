"""
@author: NakamuraShippo
@title: ComfyUI-PromptList
@description: Custom node to manage prompts in CSV
"""

from .ComfyUI_PromptList import ComfyUI_PromptList

NODE_CLASS_MAPPINGS = {
    "ComfyUI-PromptList": ComfyUI_PromptList
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI-PromptList": "Prompt List"
}

WEB_DIRECTORY = "./web"

print("ComfyUI-PromptList initialized")

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]