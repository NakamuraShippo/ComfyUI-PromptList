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
   https://github.com/NakamuraShippo/ComfyUI-PromptList
3. インストールが完了したら、ComfyUIを再起動

[ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)をインストールしていない場合
1. ComfyUIのカスタムノードディレクトリに移動します。（通常は ComfyUI/custom_nodes/）
2. このリポジトリをクローンします。  
`git clone https://github.com/NakamuraShippo/ComfyUI-PromptList`
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
  
### [prompts.yaml編集用スプレッドシート](https://docs.google.com/spreadsheets/d/1f4-kQ2YnETfa_peiRiskK3abuR4LqCTHxDwrpVqCYpY/edit?usp=sharing)を用意しました。

#### スプレッドシートを利用する前準備
1. ファイル -> コピー作成 -> 好きなファイル名に編集し「コピーを作成」
2. しばらく待つとヘルプの右側に「エクスポート」が現れるので、エクスポート -> YAMLとしてエクスポート
3. 認証が必要ですウインドウ -> OK
4. googleアカウントを選択してログイン(警告が出た場合:詳細を表示 -> 安全ではないページに移動 -> 許可)  

#### スプレッドシートの記述方法
![spreadsheets](https://github.com/NakamuraShippo/ComfyUI-PromptList/blob/main/images/spreadsheets.png)
「prompt name」のセル = prompt name  
「positive」の右隣のセル = positive prompt  
「negative」の右隣のセル = negative prompt  
をそれぞれ入力します。(A列とC列の白色セルが入力可能なセルとなっています)  
  
登録する項目を増やしたい時はオートフィルをご利用ください。  
![autofill](https://github.com/NakamuraShippo/ComfyUI-PromptList/blob/main/images/autofill.gif)

*注意*  
グレーで塗りつぶされたセルは編集しないでください。  

#### YAMLのエクスポート
1. しばらく待つとヘルプの右側に「エクスポート」が現れるので、エクスポート/インポート -> エクスポート -> エクスポート完了
2. ご自身のgoogleドライブにprompts.yamlが出力されます。

#### YAMLのインポート
1. スプレッドシートと同じフォルダ内にprompts.yamlを配置
2. エクスポート/インポート -> インポート -> インポート完了

#### 推奨する使い方
以下の設定をした上でyamlのエクスポートを行うとファイルの移動の手間がなく楽が出来ますよ。
1. googleドライブをインストール
2. prompts.yamlを当カスタムノードのフォルダ内にシンボリックリンクを設定する
3. googleドライブ内のprompts.yamlが更新されると10秒前後でデスクトップ内のファイルも同期されます。
4. やったぜ。

##### シンボリックリンクについて(知らない人向け)
ショートカットのようなものですが、決定的な違いは実体があるかのように振舞う事ができることです。
コマンドプロンプトを開き、リンクを皆さんの環境に合った箇所に書き換えて実行してください。
~~~
windows
mklink 当カスタムノードのprompts.yamlのパス GoogleDrive内のprompts.yamlファイルのパス

Mac/Linux
ln -s GoogleDrive内のprompts.yamlファイルのパス 当カスタムノードのprompts.yamlのパス

例
mklink E:\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-PromptList\prompts.yaml Y:\マイドライブ\ComfyUI-PromptList\prompts.yaml
~~~
windowsの場合はpowertoysという公式のアプリを導入すると右クリックで簡単に設定できたりもします。
探してみてね
  
## 注意事項

プロンプトリストはprompts.yamlファイルに保存されます。
編集したり新しいプロンプトを追加または編集を行った場合、変更を反映させる為にComfyUIのメインメニューにあるRefreshを押してください。

## アップデート履歴
2024/09/05 prompts.yamlを任意のフォルダで管理できるようにしました。編集用スプレッドシートも公開。
2024/08/24 とりあえず動いてるので公開

## ライセンス
このプロジェクトは MIT ライセンスに基づいてリリースされています。詳細については、[LICENSE.txt](https://github.com/NakamuraShippo/ComfyUI-PromptList/blob/main/License.txt)ファイルを参照してください。  
元の著作権表示と免責事項を含める限りは、このソフトウェアを個人的および商業的な目的で自由に使用、変更、配布できます。

## その他
バグレポートや機能リクエストは、連絡が取れる手段であれば何でも構いません。
プルリクエストも歓迎します。

## 連絡先
[NakamuraShippo](https://lit.link/admin/creator)
