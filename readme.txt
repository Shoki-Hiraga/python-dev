C:\Users\hiraga\Desktop\Python-dev
C:\Users\main\Desktop\Python-dev

git clone https://github.com/Shoki-Hiraga/python-dev
git init
 このフォルダをGitで管理できるようにコマンド実行
git add .
 全てのファイルをGitで追跡するように設定
git commit -m "リファクタリング"
 変更をコミットして、メッセージを付ける
git remote add origin https://github.com/Shoki-Hiraga/python-dev.git
 リモートリポジトリ接続
git push -u origin main
 リモートリポジトリにプッシュ

/Python-dev\setting_file\json_file
/Python-dev\setting_file\yaml_file
は個別でgit外管理

setting_file.7z のパスワードは90Cbのやつ