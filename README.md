普通の人はexeをダウンロードしてご利用ください。
使い方はexe起動 -> タスクトレイに丸い円が書いてあるアイコンが追加されているので、それを右クリックして電力プランを選ぶだけです。

◯ Python環境がある人向け

GUIDが違って使えない可能性があるので、使えなかった場合はcmdでpowercfg -Lと入力し、出力されたデータに合わせてToggle_power.pyの6~9行目をご自身で編集してください。
必要ライブラリはpystrayとpillowです。

ライブラリのインストールコマンド
pip install pystray pillow

実行する際はtoggle_power.pyのおいてあるディレクトリをcmdで開き、py toggle_power.pyで実行されます。

◯ exe化したい場合

必要ライブラリはpyinstallerのみです。
コマンドは pip install pyinstaller

toggle_power.pyのディレクトリをcmdで開き、
pyinstaller --onefile --noconsole toggle_power.py
でdistファイルができて、その中にtoggle_power.exeができているはずです。
あとはそれを実行すればOK

--onefileは単一の exe ファイルにまとめる

--noconsoleはコンソール画面を出さずに実行する　という意味です。
