# ComfyUI-PromptList
ComfyUI-PromptList is a simple prompt management node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that outputs prompts recorded in prompts.yaml.

[日本語Readme](https://github.com/NakamuraShippo/ComfyUI-PromptList/blob/main/README.md)  
  
## Features
- Reads prompts from prompts.yaml and outputs positive and negative prompts as String format.
- Writes new prompts to yaml.
- Modifies prompts registered in yaml.

## Installation
If you have installed [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager):
1. Click Manager -> Install via Git URL in the main menu.
2. Paste the URL into the text box that appears at the top of the window and press OK.  
   https://github.com/yourusername/ComfyUI-PromptList.git
3. After installation is complete, restart ComfyUI.

If you have not installed [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager):
1. Navigate to ComfyUI's custom node directory. (Usually ComfyUI/custom_nodes/)
2. Clone this repository.  
`git clone https://github.com/yourusername/ComfyUI-PromptList.git`
3. Restart ComfyUI.

## Usage
![node](https://github.com/NakamuraShippo/ComfyUI-PromptList/blob/main/images/node1.png)  
Right-click on the workspace -> Add node -> prompt -> Prompt List to add the node.  
  
The node has the following inputs:  
selection: List of prompts registered in prompts.yaml, outputs the prompt of the selected item.  
  
If the following items are filled, the prompt from selection will not be output, instead the input prompt will be output:  
Prompt Name: New prompt name or name of prompt to update  
Positive Prompt: Content of positive prompt  
Negative Prompt: Content of negative prompt  
  
The input prompt name and prompts are saved in prompts.yaml.  
Also, if you change the prompt using the same Prompt Name, it will overwrite the prompt in prompts.yaml.

### prompts.yaml format  
```yaml
test:
  positive: positive prompt
  negative: negative prompt
...
```
   
## Notes
The prompt list is saved in the prompts.yaml file.
If you edit, add new prompts, or make changes, please press Refresh in ComfyUI's main menu to reflect the changes.

## Update History
2024/08/24 Initial release as it's working for now

## License
This project is released under the MIT License.

## Other
Bug reports and feature requests are welcome through any available contact method.
Pull requests are also welcome.

## Contact
[NakamuraShippo](https://lit.link/admin/creator)
