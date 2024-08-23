# ComfyUI-PromptList
ComfyUI-PromptListは、ComfyUI用のカスタムノードで、プロンプトの管理とYAMLファイルとの連携を容易にします。

## 機能

- prompts.yamlからプロンプトを読み込み、ポジティブプロンプトとネガティブプロンプトをそれぞれString形式で出力します。
- 新しいプロンプトをyamlへ書き込む
- 既存のプロンプトの修正

## インストール
[ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)をインストールしている場合
1. メインメニューのManager -> Install via Git URLの順にクリックする
2. https://github.com/yourusername/ComfyUI-PromptList.git
   このURLを貼り付けてOKを押す
3. インストールが完了したら、ComfyUIを再起動

ComfyUI-Managerをインストールしていない場合
1. ComfyUIのカスタムノードディレクトリに移動します。（通常は ComfyUI/custom_nodes/）
2. このリポジトリをクローンします。  
git clone https://github.com/yourusername/ComfyUI-PromptList.git
3. ComfyUIを再起動します。

## 使用方法

ComfyUIワークスペースにComfyUI-PromptListノードを追加します。
ノードには以下の入力があります：

selection: 既存のプロンプトを選択するドロップダウンリスト
Prompt Name: 新しいプロンプト名または更新するプロンプト名
Positive Prompt: ポジティブプロンプトの内容
Negative Prompt: ネガティブプロンプトの内容


既存のプロンプトを使用するには、selection ドロップダウンリストから選択します。
新しいプロンプトを追加するには、Prompt Name、Positive Prompt、Negative Prompt フィールドに入力し、ノードを実行します。
既存のプロンプトを更新するには、更新したいプロンプトの名前を Prompt Name フィールドに入力し、新しい内容を Positive Prompt と Negative Prompt フィールドに入力してノードを実行します。

## 注意事項

プロンプトリストはCSVファイル（list.csv）に保存されます。このファイルは手動で編集することもできますが、ノードを通じて管理することをお勧めします。
CSVファイルを手動で編集した場合、変更を反映させるにはComfyUIを再起動するか、ノードを再読み込みする必要があります。

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。

## その他
バグレポートや機能リクエストは、連絡が取れる手段であれば何でも構いません。
プルリクエストも歓迎します。
