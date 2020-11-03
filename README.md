# QGISCustomProfiles

ポータブル版QGISにコピーして使用するカスタムプロファイルです。

## 適用手順
各プロファイル用の起動バッチ及び設定ファイルをポータブル版QGISのフォルダ内にコピーして使用します。
適宜以下に示す起動バッチの設定項目を変更してご利用ください。

### 起動バッチの説明
例としてnakedQGIS.bat  
```bat
REM @echo off
SET DIR=%~dp0
call "%DIR%bin\qgis-ltr.bat" ^
--profiles-path "%DIR:~0,-1%" ^
--profile naked ^
--project "%DIR%projects\sample.qgs"
REM @echo on
```

`--profiles-path "%DIR:~0,-1%"` : プロファイルの場所をポータブル版QGISのフォルダの直下に指定しています。  
`--profile naked` : プロファイル名を「naked」に指定しています。  
この設定で<ポータブル版QGISフォルダ>\profiles\nakedに設定ファイルが格納されます。

`--project "%DIR%projects\sample.qgs"` : 読み込むQGISプロジェクトファイルを指定しています。   
この設定で<ポータブル版QGISフォルダ>\projects\sample.qgsを読み込みます。  


### 設定ファイルの説明
`profiles\<profile_name>\QGIS\QGIS3.ini`  
QGISの全般的な設定が書き込まれています。  
このQGISCustomProfilesではアプリケーションや起動プラグインの設定を行っています。

`profiles\<profile_name>\QGIS\QGISCUSTOMIZATION3.ini`  
主にQGISのインターフェースのカスタマイズで設定した内容が書き込まれています。  
このQGISCustomProfilesではメニューバーやツールバー、ステータスバーなどの表示設定を行っています。

---

## 各プロファイル

### nakedQGIS

地図だけが表示されるよう制御したプロファイルです。  
全画面表示(F11)にすることで画面全体を地図として使用できます。


### simpleQGIS

地図表示アプリケーションとして最低限必要と思われる機能に限定したプロファイルです。
* ナビゲーションツールバー
  * 地図を移動
  * 拡大
  * 縮小
  * 全域表示
* 属性ツールバー
  * 地物情報表示
* プラグインツールバー
  * EZPrinter（地図のPDF出力）
  * LayerPanelButton（レイヤパネルの表示切替）

