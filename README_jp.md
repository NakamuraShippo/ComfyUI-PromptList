# ComfyUI-PromptList
ComfyUI-PromptListは、[ComfyUI](https://github.com/comfyanonymous/ComfyUI)用のprompts.yamlに記録したプロンプトを出力するシンプルなプロンプト管理ノードです。

## 機能

- prompts.yamlからプロンプトを読み込み、ポジティブプロンプトとネガティブプロンプトをそれぞれString形式で出力します。
- 新しいプロンプトをyamlへ書き込む
- yamlに登録されているプロンプトの修正

## インストール
[ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)をインストールしている場合
1. メインメニューのManager -> Install via Git URLの順にクリックする
2. ウインドウ上部に出てくるテキストボックスにURLを貼り付けてOKを押す  
   https://github.com/yourusername/ComfyUI-PromptList.git
3. インストールが完了したら、ComfyUIを再起動

[ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)をインストールしていない場合
1. ComfyUIのカスタムノードディレクトリに移動します。（通常は ComfyUI/custom_nodes/）
2. このリポジトリをクローンします。  
`git clone https://github.com/yourusername/ComfyUI-PromptList.git`
3. ComfyUIを再起動します。

## 使用方法
![node](https://github.com/NakamuraShippo/ComfyUI-PromptList/blob/main/images/node1.png)  
ワークスペース上で右クリック -> Add node-> prompt -> Prompt Listでノードを追加します。  
  
ノードには以下の入力があります：  
selection: prompts.yamlに登録されているプロンプトリスト、選択した項目のプロンプトを出力します。  
  
以下の項目に入力されている場合はselectionのプロンプトは出力されずに入力したプロンプトが出力されます。  
Prompt Name: 新しいプロンプト名または更新するプロンプト名  
Positive Prompt: ポジティブプロンプトの内容  
Negative Prompt: ネガティブプロンプトの内容  
  
入力したプロンプト名とプロンプトはprompts.yamlに保存されます。  
また、同名のPrompt Nameを使用してプロンプトを変更した場合はprompts.yaml内のプロンプトを上書きします。 

### prompts.yamlのフォーマット  
~~~prompts.yaml
prompt name:
  positive: positive prompt
  negative: negative prompt
...
~~~
   
## 注意事項

プロンプトリストはprompts.yamlファイルに保存されます。
編集したり新しいプロンプトを追加または編集を行った場合、変更を反映させる為にComfyUIのメインメニューにあるRefreshを押してください。

## アップデート履歴
2024/08/24 とりあえず動いてるので公開

## ライセンス
このプロジェクトは MIT ライセンスに基づいてリリースされています。詳細については、[LICENSE.txt](https://github.com/NakamuraShippo/ComfyUI-PromptList/blob/main/License.txt)ファイルを参照してください。  
元の著作権表示と免責事項を含める限りは、このソフトウェアを個人的および商業的な目的で自由に使用、変更、配布できます。

## その他
バグレポートや機能リクエストは、連絡が取れる手段であれば何でも構いません。
プルリクエストも歓迎します。

## 連絡先
[NakamuraShippo](https://lit.link/admin/creator)
