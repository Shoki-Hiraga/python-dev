from setting_file.header import *


# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定
file_name = "Gscraped_data.csv"
output_file = os.path.join(file_directory, file_name)

# # スプレッドシート認証
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# credentials = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/STAFF1088/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/python-scrape.json", scope)
# gc = gspread.authorize(credentials)
# ヘッダー行の設定。ここではウェブページからスクレイプする項目名を列挙しています


header_row = ['URL', 'メーカー', '車種タイトル', '車輌本体価格(basePrice__content)', '走行距離', '年式(specList__jpYear)', '修復歴']

urls = [
'https://www.gaisha-oh.com/us/chevrolet/ssr/',
'https://www.gaisha-oh.com/us/chrysler/vision/',
'https://www.gaisha-oh.com/germany/porsche/panamera_s_e_hybrid/',
'https://www.gaisha-oh.com/italy/ferrari/laferrari/',
'https://www.gaisha-oh.com/germany/bmw/5series_sedan_phv/',
'https://www.gaisha-oh.com/germany/porsche/cayenne_e_hybrid/',
'https://www.gaisha-oh.com/germany/porsche/cayenne_coupe/',
'https://www.gaisha-oh.com/sweden/volvo/xc40_pluginhybrid/',
'https://www.gaisha-oh.com/germany/porsche/carrera_gt/',
'https://www.gaisha-oh.com/us/lincoln/aviator/',
'https://www.gaisha-oh.com/germany/porsche/panamera_sportturismo/',
'https://www.gaisha-oh.com/us/chevrolet/volt/',
'https://www.gaisha-oh.com/france/peugeot/107/',
'https://www.gaisha-oh.com/us/cadillac/cts_v/',
'https://www.gaisha-oh.com/france/peugeot/e-2008/',
'https://www.gaisha-oh.com/italy/fiat/x1-9/',
'https://www.gaisha-oh.com/germany/amg/gclass/',
'https://www.gaisha-oh.com/germany/benz/glc_coupe_plugin_hybrid/',
'https://www.gaisha-oh.com/germany/volkswagen/golf_r_variant/',
'https://www.gaisha-oh.com/us/chevrolet/shiebetto/',
'https://www.gaisha-oh.com/germany/bmw/x5_m/',
'https://www.gaisha-oh.com/germany/audi/a5/',
'https://www.gaisha-oh.com/france/peugeot/e-208/',
'https://www.gaisha-oh.com/uk/daimler/super_v8/',
'https://www.gaisha-oh.com/italy/lamborghini/huracan_spider/',
'https://www.gaisha-oh.com/germany/amg/cclass/',
'https://www.gaisha-oh.com/germany/benz/s_class_hybrid/',
'https://www.gaisha-oh.com/uk/astonmartin/vanquish_volante/',
'https://www.gaisha-oh.com/germany/amg/eclass_sedan/',
'https://www.gaisha-oh.com/germany/benz/c_class_estate_plugin_hybrid/',
'https://www.gaisha-oh.com/germany/volkswagen/cc/',
'https://www.gaisha-oh.com/korea/hyundai/xg/',
'https://www.gaisha-oh.com/germany/bmw/x6_hybrid/',
'https://www.gaisha-oh.com/germany/amg/cwagon/',
'https://www.gaisha-oh.com/germany/bmw/z4_m_roadster/',
'https://www.gaisha-oh.com/germany/audi/allroad_quattro/',
'https://www.gaisha-oh.com/germany/bmw/3series_sedan/',
'https://www.gaisha-oh.com/italy/fiat/124/',
'https://www.gaisha-oh.com/france/ds_automobiles/om_ds5/',
'https://www.gaisha-oh.com/uk/jaguar/xk_convertible/',
'https://www.gaisha-oh.com/germany/amg/ewagon/',
'https://www.gaisha-oh.com/germany/bmw/3series_sedan_hybrid/',
'https://www.gaisha-oh.com/korea/hyundai/nexo/',
'https://www.gaisha-oh.com/italy/fiat/124_spider/',
'https://www.gaisha-oh.com/uk/astonmartin/db9_volante/',
'https://www.gaisha-oh.com/korea/hyundai/jm/',
'https://www.gaisha-oh.com/germany/volkswagen/golf_alltrack/',
'https://www.gaisha-oh.com/france/renault/megane_hatchback/',
'https://www.gaisha-oh.com/germany/volkswagen/polo_gti/',
'https://www.gaisha-oh.com/italy/alfaromeo/mito/',
'https://www.gaisha-oh.com/germany/audi/cabriolet/',
'https://www.gaisha-oh.com/germany/porsche/panamera_e_hybrid/',
'https://www.gaisha-oh.com/germany/porsche/718_cayman_gt4/',
'https://www.gaisha-oh.com/korea/hyundai/tb/',
'https://www.gaisha-oh.com/sweden/volvo/960series/',
'https://www.gaisha-oh.com/us/gmc/suburban/',
'https://www.gaisha-oh.com/uk/landrover/range_rover_phev/',
'https://www.gaisha-oh.com/italy/fiat/new_barchetta/',
'https://www.gaisha-oh.com/france/renault/kryospol/',
'https://www.gaisha-oh.com/germany/volkswagen/passat_wagon/',
'https://www.gaisha-oh.com/sweden/saab/9_5_sedan/',
'https://www.gaisha-oh.com/sweden/volvo/c40_recharge/',
'https://www.gaisha-oh.com/germany/benz/cl_class/',
'https://www.gaisha-oh.com/germany/volkswagen/type_2/',
'https://www.gaisha-oh.com/italy/lamborghini/aventador/',
'https://www.gaisha-oh.com/germany/porsche/718_boxster/',
'https://www.gaisha-oh.com/uk/rolls-royce/silverspur_withdivision/',
'https://www.gaisha-oh.com/us/chevrolet/optra_sedan/',
'https://www.gaisha-oh.com/germany/audi/a1_sportback/',
'https://www.gaisha-oh.com/germany/bmw/2series/',
'https://www.gaisha-oh.com/us/ford/capri/',
'https://www.gaisha-oh.com/germany/volkswagen/t_roc/',
'https://www.gaisha-oh.com/germany/amg/mclass/',
'https://www.gaisha-oh.com/germany/volkswagen/arteon_shooting_brake/',
'https://www.gaisha-oh.com/us/ford/focus_wagon/',
'https://www.gaisha-oh.com/italy/maserati/spyder/',
'https://www.gaisha-oh.com/germany/audi/a3/',
'https://www.gaisha-oh.com/germany/bmw/5series_sedan/',
'https://www.gaisha-oh.com/italy/ferrari/355_f1/',
'https://www.gaisha-oh.com/france/citroen/gs/',
'https://www.gaisha-oh.com/france/renault/avantime/',
'https://www.gaisha-oh.com/germany/bmw/m5_competition/',
'https://www.gaisha-oh.com/uk/jaguar/xj_s/',
'https://www.gaisha-oh.com/germany/audi/a6_hybrid/',
'https://www.gaisha-oh.com/sweden/volvo/xc90/',
'https://www.gaisha-oh.com/germany/benz/c_sports_coupe/',
'https://www.gaisha-oh.com/italy/lancia/l_ypsilon/',
'https://www.gaisha-oh.com/us/ford/galaxy/',
'https://www.gaisha-oh.com/germany/audi/q4-e-tron/',
'https://www.gaisha-oh.com/germany/bmw/2series_gran_coupe/',
'https://www.gaisha-oh.com/germany/audi/tt_rs_pluscoupe/',
'https://www.gaisha-oh.com/germany/mini/crossover_phev/',
'https://www.gaisha-oh.com/germany/amg/c_class_cabriolet/',
'https://www.gaisha-oh.com/germany/benz/m_class/',
'https://www.gaisha-oh.com/us/chrysler/premier/',
'https://www.gaisha-oh.com/germany/amg/glclass/',
'https://www.gaisha-oh.com/germany/benz/eqc/',
'https://www.gaisha-oh.com/uk/rolls-royce/silverspur_2/',
'https://www.gaisha-oh.com/germany/bmw/7series_sedan_hybrid/',
'https://www.gaisha-oh.com/us/ford/ranger/',
'https://www.gaisha-oh.com/italy/maserati/430series/',
'https://www.gaisha-oh.com/france/ds_automobiles/om_ds4/',
'https://www.gaisha-oh.com/germany/volkswagen/golf_r/',
'https://www.gaisha-oh.com/germany/bmw/z1/',
'https://www.gaisha-oh.com/france/peugeot/206series/',
'https://www.gaisha-oh.com/italy/autobianchi/a112/',
'https://www.gaisha-oh.com/italy/lancia/musa/',
'https://www.gaisha-oh.com/france/peugeot/207_hatchback/',
'https://www.gaisha-oh.com/us/chrysler/town_and_country/',
'https://www.gaisha-oh.com/us/chevrolet/corvair/',
'https://www.gaisha-oh.com/uk/jaguar/sovereign/',
'https://www.gaisha-oh.com/france/renault/25series/',
'https://www.gaisha-oh.com/uk/rover/r_mini/',
'https://www.gaisha-oh.com/germany/volkswagen/scirocco/',
'https://www.gaisha-oh.com/france/peugeot/508_sedan/',
'https://www.gaisha-oh.com/italy/abarth/595_c/',
'https://www.gaisha-oh.com/germany/audi/a4/',
'https://www.gaisha-oh.com/germany/bmw/m6_cabriolet/',
'https://www.gaisha-oh.com/uk/landrover/defender/',
'https://www.gaisha-oh.com/italy/lamborghini/lm002/',
'https://www.gaisha-oh.com/germany/audi/s8_plus/',
'https://www.gaisha-oh.com/germany/benz/a_class_sedan/',
'https://www.gaisha-oh.com/italy/maserati/biturbo/',
'https://www.gaisha-oh.com/italy/maserati/royal/',
'https://www.gaisha-oh.com/uk/bentley/continental_convertible/',
'https://www.gaisha-oh.com/southafrica/birkin/b_super_7/',
'https://www.gaisha-oh.com/us/lincoln/mark_7/',
'https://www.gaisha-oh.com/italy/fiat/127/',
'https://www.gaisha-oh.com/germany/audi/tt_rs_roadster/',
'https://www.gaisha-oh.com/uk/rolls-royce/silvershadow/',
'https://www.gaisha-oh.com/sweden/saab/9_5series/',
'https://www.gaisha-oh.com/germany/bmw/x3_m/',
'https://www.gaisha-oh.com/germany/bmw/z3_m_roadster/',
'https://www.gaisha-oh.com/us/chevrolet/s_10/',
'https://www.gaisha-oh.com/germany/bmw/x1/',
'https://www.gaisha-oh.com/france/renault/r_alpine/',
'https://www.gaisha-oh.com/germany/volkswagen/lupo/',
'https://www.gaisha-oh.com/germany/audi/a1/',
'https://www.gaisha-oh.com/sweden/volvo/780series/',
'https://www.gaisha-oh.com/germany/amg/ccoupe/',
'https://www.gaisha-oh.com/germany/audi/s4_avant/',
'https://www.gaisha-oh.com/germany/bmw/m4_cabriolet/',
'https://www.gaisha-oh.com/france/renault/trafic/',
'https://www.gaisha-oh.com/france/citroen/c5_aircross/',
'https://www.gaisha-oh.com/germany/amg/scoupe/',
'https://www.gaisha-oh.com/germany/audi/r8_spyder/',
'https://www.gaisha-oh.com/germany/mini/crossover/',
'https://www.gaisha-oh.com/germany/bmw/xm/',
'https://www.gaisha-oh.com/us/gmc/gc_1500/',
'https://www.gaisha-oh.com/germany/benz/c_class_sedan/',
'https://www.gaisha-oh.com/uk/landrover/discovery/',
'https://www.gaisha-oh.com/italy/alfaromeo/147series/',
'https://www.gaisha-oh.com/italy/fiat/ritmo/',
'https://www.gaisha-oh.com/germany/volkswagen/passat_alltrack/',
'https://www.gaisha-oh.com/uk/astonmartin/v12_vantage_roadster/',
'https://www.gaisha-oh.com/uk/bentley/turbo/',
'https://www.gaisha-oh.com/germany/volkswagen/t5_california/',
'https://www.gaisha-oh.com/germany/audi/s5_cabriolet/',
'https://www.gaisha-oh.com/uk/bentley/continental_coupe/',
'https://www.gaisha-oh.com/sweden/saab/9_3series/',
'https://www.gaisha-oh.com/germany/amg/clkcabriolet/',
'https://www.gaisha-oh.com/us/chevrolet/blazer/',
'https://www.gaisha-oh.com/germany/bmw/3series/',
'https://www.gaisha-oh.com/germany/audi/r8/',
'https://www.gaisha-oh.com/germany/benz/sl/',
'https://www.gaisha-oh.com/uk/bentley/bentayga/',
'https://www.gaisha-oh.com/germany/audi/a_coupe/',
'https://www.gaisha-oh.com/sweden/volvo/v40_cross_country/',
'https://www.gaisha-oh.com/italy/fiat/500l/',
'https://www.gaisha-oh.com/france/renault/express_r/',
'https://www.gaisha-oh.com/italy/ferrari/360series/',
'https://www.gaisha-oh.com/germany/audi/s6/',
'https://www.gaisha-oh.com/us/chevrolet/corvette_convertible/',
'https://www.gaisha-oh.com/france/peugeot/607series/',
'https://www.gaisha-oh.com/germany/porsche/911series/',
'https://www.gaisha-oh.com/germany/porsche/boxster/',
'https://www.gaisha-oh.com/germany/bmw/m8_coupe/',
'https://www.gaisha-oh.com/southafrica/birkin/birkin_7/',
'https://www.gaisha-oh.com/germany/benz/eqb/',
'https://www.gaisha-oh.com/germany/audi/a4_avant/',
'https://www.gaisha-oh.com/germany/amg/clsclass/',
'https://www.gaisha-oh.com/germany/volkswagen/new_beetle_cabriolet/',
'https://www.gaisha-oh.com/us/cadillac/coupe_deville/',
'https://www.gaisha-oh.com/france/citroen/xantia_break/',
'https://www.gaisha-oh.com/italy/abarth/695_biposto/',
'https://www.gaisha-oh.com/germany/volkswagen/golf_wagon/',
'https://www.gaisha-oh.com/germany/bmw/z4_coupe/',
'https://www.gaisha-oh.com/germany/bmw/2series_gran_tourer/',
'https://www.gaisha-oh.com/us/dodge/caravan/',
'https://www.gaisha-oh.com/germany/bmw/3series_gran_turismo/',
'https://www.gaisha-oh.com/germany/bmw/z3_m_coupe/',
'https://www.gaisha-oh.com/italy/lamborghini/aventador_roadster/',
'https://www.gaisha-oh.com/germany/bmw/2series_active_tourer/',
'https://www.gaisha-oh.com/germany/bmw/i8_roadster/',
'https://www.gaisha-oh.com/us/lincoln/l_continental/',
'https://www.gaisha-oh.com/france/ds_automobiles/om_ds4_crossback/',
'https://www.gaisha-oh.com/us/ford/mustang_convertible/',
'https://www.gaisha-oh.com/germany/audi/a6_allroad_quattro/',
'https://www.gaisha-oh.com/uk/astonmartin/dbs_superleggera_volante/',
'https://www.gaisha-oh.com/us/chrysler/voyager/',
'https://www.gaisha-oh.com/us/ford/econoline/',
'https://www.gaisha-oh.com/germany/volkswagen/cross_touran/',
'https://www.gaisha-oh.com/italy/alfaromeo/4c_spider/',
'https://www.gaisha-oh.com/germany/bmw/1series/',
'https://www.gaisha-oh.com/us/ford/fseries_150/',
'https://www.gaisha-oh.com/italy/lancia/lybra/',
'https://www.gaisha-oh.com/france/peugeot/306_hatchback/',
'https://www.gaisha-oh.com/germany/benz/gle_coupe/',
'https://www.gaisha-oh.com/france/citroen/c5/',
'https://www.gaisha-oh.com/uk/astonmartin/dbs/',
'https://www.gaisha-oh.com/italy/alfaromeo/alfa_spider/',
'https://www.gaisha-oh.com/germany/audi/s4/',
'https://www.gaisha-oh.com/germany/audi/q4/',
'https://www.gaisha-oh.com/germany/volkswagen/cross_up/',
'https://www.gaisha-oh.com/uk/astonmartin/vanquish_s/',
'https://www.gaisha-oh.com/germany/amg/clkclass/',
'https://www.gaisha-oh.com/us/ford/fordgt_40/',
'https://www.gaisha-oh.com/italy/ferrari/488pista/',
'https://www.gaisha-oh.com/sweden/saab/9_3_sportsedan/',
'https://www.gaisha-oh.com/uk/lotus/europa/',
'https://www.gaisha-oh.com/uk/astonmartin/cygnet/',
'https://www.gaisha-oh.com/germany/porsche/928series/',
'https://www.gaisha-oh.com/germany/benz/gls/',
'https://www.gaisha-oh.com/france/renault/lutecia/',
'https://www.gaisha-oh.com/germany/audi/q3_sportback/',
'https://www.gaisha-oh.com/germany/audi/tt_rs_coupe/',
'https://www.gaisha-oh.com/korea/hyundai/i30/',
'https://www.gaisha-oh.com/germany/bmw/5series_touring/',
'https://www.gaisha-oh.com/sweden/saab/9000series/',
'https://www.gaisha-oh.com/italy/alfaromeo/8c_spider/',
'https://www.gaisha-oh.com/us/lincoln/mkz/',
'https://www.gaisha-oh.com/uk/astonmartin/v8_vantage_roadster/',
'https://www.gaisha-oh.com/france/citroen/ds3_cabrio/',
'https://www.gaisha-oh.com/us/dodge/van/',
'https://www.gaisha-oh.com/germany/volkswagen/vento/',
'https://www.gaisha-oh.com/germany/mini/mroadster/',
'https://www.gaisha-oh.com/germany/porsche/944_cabriolet/',
'https://www.gaisha-oh.com/germany/audi/e-tron/',
'https://www.gaisha-oh.com/germany/benz/slk_class/',
'https://www.gaisha-oh.com/us/chevrolet/tahoe_sports/',
'https://www.gaisha-oh.com/germany/bmw/x4_m/',
'https://www.gaisha-oh.com/germany/benz/glc_plugin_hybrid/',
'https://www.gaisha-oh.com/france/citroen/spacetourer/',
'https://www.gaisha-oh.com/germany/bmw/3series_touring/',
'https://www.gaisha-oh.com/germany/porsche/911_cabriolet/',
'https://www.gaisha-oh.com/germany/bmw/ix/',
'https://www.gaisha-oh.com/italy/lamborghini/diablo/',
'https://www.gaisha-oh.com/germany/benz/e_wagon/',
'https://www.gaisha-oh.com/germany/bmw/x2/',
'https://www.gaisha-oh.com/france/citroen/c4_cactus/',
'https://www.gaisha-oh.com/germany/audi/e-tron_sportback/',
'https://www.gaisha-oh.com/france/renault/megane_sports_tourer/',
'https://www.gaisha-oh.com/germany/bmw/z3_coupe/',
'https://www.gaisha-oh.com/us/gmc/sierra_c/',
'https://www.gaisha-oh.com/germany/mini/clubman/',
'https://www.gaisha-oh.com/france/citroen/2_cv/',
'https://www.gaisha-oh.com/germany/bmw/m6/',
'https://www.gaisha-oh.com/us/chrysler/300m/',
'https://www.gaisha-oh.com/sweden/volvo/v60_cross_country/',
'https://www.gaisha-oh.com/uk/astonmartin/vantage/',
'https://www.gaisha-oh.com/france/peugeot/205_cabriolet/',
'https://www.gaisha-oh.com/germany/benz/g_class_cabriolet/',
'https://www.gaisha-oh.com/germany/benz/slc/',
'https://www.gaisha-oh.com/us/dodge/challenger/',
'https://www.gaisha-oh.com/uk/astonmartin/db9/',
'https://www.gaisha-oh.com/uk/rolls-royce/wraith/',
'https://www.gaisha-oh.com/france/peugeot/208series/',
'https://www.gaisha-oh.com/france/renault/sport-spider/',
'https://www.gaisha-oh.com/italy/lamborghini/jota/',
'https://www.gaisha-oh.com/france/peugeot/406_sedan/',
'https://www.gaisha-oh.com/germany/audi/a6_avant/',
'https://www.gaisha-oh.com/germany/volkswagen/golf_cabrio/',
'https://www.gaisha-oh.com/us/lincoln/towncar/',
'https://www.gaisha-oh.com/germany/audi/rsq3_sportback/',
'https://www.gaisha-oh.com/sweden/volvo/xc40_recharge/',
'https://www.gaisha-oh.com/france/citroen/zx_coupe/',
'https://www.gaisha-oh.com/italy/alfaromeo/8c/',
'https://www.gaisha-oh.com/us/chevrolet/cheviban/',
'https://www.gaisha-oh.com/italy/ferrari/dino/',
'https://www.gaisha-oh.com/germany/benz/glc_coupe/',
'https://www.gaisha-oh.com/germany/amg/eclass/',
'https://www.gaisha-oh.com/germany/audi/s3_sportback/',
'https://www.gaisha-oh.com/us/ford/crownvictoria/',
'https://www.gaisha-oh.com/germany/volkswagen/touareg/',
'https://www.gaisha-oh.com/france/citroen/grand_c4_spacetourer/',
'https://www.gaisha-oh.com/germany/volkswagen/tiguan/',
'https://www.gaisha-oh.com/france/peugeot/308_hatchback/',
'https://www.gaisha-oh.com/italy/abarth/695_edizione_maserati/',
'https://www.gaisha-oh.com/us/dodge/caliber/',
'https://www.gaisha-oh.com/france/citroen/zx_break/',
'https://www.gaisha-oh.com/germany/audi/s3_sedan/',
'https://www.gaisha-oh.com/italy/fiat/new_panda/',
'https://www.gaisha-oh.com/germany/bmw/3series_compact/',
'https://www.gaisha-oh.com/uk/astonmartin/vanquish/',
'https://www.gaisha-oh.com/france/citroen/grand_c4_picasso/',
'https://www.gaisha-oh.com/france/peugeot/508series/',
'https://www.gaisha-oh.com/italy/alfaromeo/gt_a/',
'https://www.gaisha-oh.com/germany/porsche/968_cabriolet/',
'https://www.gaisha-oh.com/germany/audi/a3_sedan/',
'https://www.gaisha-oh.com/germany/amg/rclass/',
'https://www.gaisha-oh.com/italy/lamborghini/huracan/',
'https://www.gaisha-oh.com/sweden/volvo/850_estate/',
'https://www.gaisha-oh.com/france/peugeot/407series/',
'https://www.gaisha-oh.com/germany/audi/q3/',
'https://www.gaisha-oh.com/germany/benz/c_class/',
'https://www.gaisha-oh.com/uk/jaguar/xj_scoupe/',
'https://www.gaisha-oh.com/france/renault/kangoo/',
'https://www.gaisha-oh.com/uk/lotus/elise/',
'https://www.gaisha-oh.com/germany/audi/s1_sportback/',
'https://www.gaisha-oh.com/germany/benz/a_class/',
'https://www.gaisha-oh.com/uk/jaguar/f_pace/',
'https://www.gaisha-oh.com/france/citroen/c5_break/',
'https://www.gaisha-oh.com/us/chrysler/imperial/',
'https://www.gaisha-oh.com/us/hummer/h3/',
'https://www.gaisha-oh.com/france/peugeot/508_sw/',
'https://www.gaisha-oh.com/germany/audi/a7/',
'https://www.gaisha-oh.com/us/gmc/vandura/',
'https://www.gaisha-oh.com/germany/benz/x_class/',
'https://www.gaisha-oh.com/france/peugeot/307series/',
'https://www.gaisha-oh.com/italy/alfaromeo/159_sport_wagon/',
'https://www.gaisha-oh.com/italy/ferrari/488series/',
'https://www.gaisha-oh.com/germany/porsche/930series/',
'https://www.gaisha-oh.com/france/citroen/zx/',
'https://www.gaisha-oh.com/germany/volkswagen/tcross/',
'https://www.gaisha-oh.com/germany/benz/c_coupe/',
'https://www.gaisha-oh.com/italy/ferrari/430_scuderia/',
'https://www.gaisha-oh.com/italy/ferrari/f430_spider/',
'https://www.gaisha-oh.com/germany/audi/a8_hybrid/',
'https://www.gaisha-oh.com/germany/bmw/z4_m_coupe/',
'https://www.gaisha-oh.com/germany/audi/tt/',
'https://www.gaisha-oh.com/italy/abarth/695series/',
'https://www.gaisha-oh.com/germany/volkswagen/beetle/',
'https://www.gaisha-oh.com/france/peugeot/407_sw/',
'https://www.gaisha-oh.com/italy/alfaromeo/166series/',
'https://www.gaisha-oh.com/germany/volkswagen/type_3/',
'https://www.gaisha-oh.com/germany/bmw/x6/',
'https://www.gaisha-oh.com/italy/lamborghini/jarama/',
'https://www.gaisha-oh.com/italy/fiat/punto_evo/',
'https://www.gaisha-oh.com/germany/bmw/1series_cabriolet/',
'https://www.gaisha-oh.com/germany/audi/100_avant/',
'https://www.gaisha-oh.com/germany/bmw/4series_coupe/',
'https://www.gaisha-oh.com/uk/jaguar/i_pace/',
'https://www.gaisha-oh.com/germany/bmw/i8/',
'https://www.gaisha-oh.com/italy/abarth/695c_rivale/',
'https://www.gaisha-oh.com/germany/audi/a2/',
'https://www.gaisha-oh.com/germany/volkswagen/bora/',
'https://www.gaisha-oh.com/italy/maserati/levante/',
'https://www.gaisha-oh.com/germany/audi/a6/',
'https://www.gaisha-oh.com/sweden/volvo/v60/',
'https://www.gaisha-oh.com/germany/audi/rs5/',
'https://www.gaisha-oh.com/germany/audi/s6_avant/',
'https://www.gaisha-oh.com/us/ford/ixion/',
'https://www.gaisha-oh.com/germany/volkswagen/touran/',
'https://www.gaisha-oh.com/uk/bentley/continental_gt_convertible/',
'https://www.gaisha-oh.com/uk/landrover/discovery_3/',
'https://www.gaisha-oh.com/us/cadillac/fleetwood_coupe/',
'https://www.gaisha-oh.com/germany/audi/q2/',
'https://www.gaisha-oh.com/germany/audi/s5_sportback/',
'https://www.gaisha-oh.com/germany/audi/rs6_avant_performance/',
'https://www.gaisha-oh.com/italy/lamborghini/jalpa/',
'https://www.gaisha-oh.com/germany/bmw/m3_sedan/',
'https://www.gaisha-oh.com/italy/lamborghini/Islero/',
'https://www.gaisha-oh.com/us/dodge/ram/',
'https://www.gaisha-oh.com/germany/mini/convertible/',
'https://www.gaisha-oh.com/germany/benz/glk_class/',
'https://www.gaisha-oh.com/germany/audi/rs3/',
'https://www.gaisha-oh.com/france/renault/laguna_wagon/',
'https://www.gaisha-oh.com/germany/audi/rs7/',
'https://www.gaisha-oh.com/germany/audi/sq2/',
'https://www.gaisha-oh.com/sweden/volvo/740series/',
'https://www.gaisha-oh.com/us/ford/bronco/',
'https://www.gaisha-oh.com/uk/jaguar/f_type_convertible/',
'https://www.gaisha-oh.com/us/gmc/safari/',
'https://www.gaisha-oh.com/italy/lamborghini/350gt/',
'https://www.gaisha-oh.com/sweden/volvo/s60/',
'https://www.gaisha-oh.com/france/peugeot/207_cc/',
'https://www.gaisha-oh.com/france/peugeot/2008series/',
'https://www.gaisha-oh.com/germany/amg/a_class/',
'https://www.gaisha-oh.com/france/peugeot/308series/',
'https://www.gaisha-oh.com/italy/maserati/biturbo_coupe/',
'https://www.gaisha-oh.com/uk/lotus/exige_sport350_roadster/',
'https://www.gaisha-oh.com/us/ford/escort/',
'https://www.gaisha-oh.com/sweden/volvo/940_estate/',
'https://www.gaisha-oh.com/germany/audi/a4_allroad_quattro/',
'https://www.gaisha-oh.com/germany/volkswagen/type_1/',
'https://www.gaisha-oh.com/germany/audi/sq5/',
'https://www.gaisha-oh.com/germany/volkswagen/passat_cc/',
'https://www.gaisha-oh.com/us/ford/festiva_miniwagon/',
'https://www.gaisha-oh.com/uk/rolls-royce/silvercloud/',
'https://www.gaisha-oh.com/germany/benz/c_class_sedan_plugin_hybrid/',
'https://www.gaisha-oh.com/germany/audi/rsq3_performance/',
'https://www.gaisha-oh.com/us/dodge/grand_caravan/',
'https://www.gaisha-oh.com/sweden/volvo/v90/',
'https://www.gaisha-oh.com/germany/audi/rs6_avant/',
'https://www.gaisha-oh.com/us/chevrolet/Impala/',
'https://www.gaisha-oh.com/italy/alfaromeo/156series/',
'https://www.gaisha-oh.com/sweden/volvo/240_estate/',
'https://www.gaisha-oh.com/us/chevrolet/silverado/',
'https://www.gaisha-oh.com/us/ford/escape/',
'https://www.gaisha-oh.com/france/renault/megane/',
'https://www.gaisha-oh.com/france/citroen/xsara/',
'https://www.gaisha-oh.com/korea/hyundai/i30cw/',
'https://www.gaisha-oh.com/sweden/volvo/120amazon/',
'https://www.gaisha-oh.com/italy/ferrari/mondial/',
'https://www.gaisha-oh.com/us/cadillac/ats/',
'https://www.gaisha-oh.com/germany/audi/rs4_avant/',
'https://www.gaisha-oh.com/uk/jaguar/f_type/',
'https://www.gaisha-oh.com/italy/ferrari/enzoferrari/',
'https://www.gaisha-oh.com/italy/ferrari/sf90stradare/',
'https://www.gaisha-oh.com/germany/bmw/ix3/',
'https://www.gaisha-oh.com/germany/porsche/718_cayman/',
'https://www.gaisha-oh.com/france/citroen/cx_wagon/',
'https://www.gaisha-oh.com/germany/bmw/6series_gran_coupe/',
'https://www.gaisha-oh.com/germany/porsche/997series/',
'https://www.gaisha-oh.com/korea/hyundai/granger/',
'https://www.gaisha-oh.com/germany/bmw/x5/',
'https://www.gaisha-oh.com/germany/benz/clk_class/',
'https://www.gaisha-oh.com/germany/bmw/m5/',
'https://www.gaisha-oh.com/italy/ferrari/328gts/',
'https://www.gaisha-oh.com/korea/hyundai/elantra/',
'https://www.gaisha-oh.com/germany/amg/s_class_cabriolet/',
'https://www.gaisha-oh.com/italy/fiat/new_multipla/',
'https://www.gaisha-oh.com/germany/audi/rs3_sedan/',
'https://www.gaisha-oh.com/italy/abarth/a_500c/',
'https://www.gaisha-oh.com/italy/ferrari/458_spider/',
'https://www.gaisha-oh.com/france/ds_automobiles/om_ds3_cabrio/',
'https://www.gaisha-oh.com/france/citroen/ax/',
'https://www.gaisha-oh.com/italy/ferrari/gtc4lusso/',
'https://www.gaisha-oh.com/italy/fiat/multipla/',
'https://www.gaisha-oh.com/italy/maserati/222series/',
'https://www.gaisha-oh.com/us/chevrolet/c_1500/',
'https://www.gaisha-oh.com/germany/audi/q5/',
'https://www.gaisha-oh.com/italy/maserati/spyder_zagato/',
'https://www.gaisha-oh.com/germany/bmw/m2_competition/',
'https://www.gaisha-oh.com/italy/fiat/128/',
'https://www.gaisha-oh.com/germany/bmw/5series_gran_turismo/',
'https://www.gaisha-oh.com/france/peugeot/308_sw/',
'https://www.gaisha-oh.com/france/citroen/c4_picasso/',
'https://www.gaisha-oh.com/sweden/volvo/v70_xc/',
'https://www.gaisha-oh.com/us/chevrolet/k10/',
'https://www.gaisha-oh.com/germany/audi/a5_sportback/',
'https://www.gaisha-oh.com/germany/volkswagen/golf_variant/',
'https://www.gaisha-oh.com/germany/benz/medium_coupe/',
'https://www.gaisha-oh.com/germany/benz/e_class/',
'https://www.gaisha-oh.com/italy/ferrari/f355_spider/'
]

# アクセスエラー発生時の最大リトライ回数を設定
MAX_RETRIES = 10

# ウェブページの情報をスクレイプする関数
def scrape_url(url):
    delay_time = random.uniform(1, 5)  # リクエスト間のランダムな遅延時間を設定
    user_agent = random.choice(user_agents)  # リクエスト用のランダムなユーザーエージェントを選択
    retry_count = 0  # リトライ回数のカウンター

    while retry_count < MAX_RETRIES:
        try:
            # ユーザーエージェントを指定してURLにリクエストを送信
            response = requests.get(url, headers={'User-Agent': user_agent})

            if response.status_code == 200:
                # 正常にアクセスできた場合は遅延を挟んでループを抜ける
                time.sleep(delay_time)
                break
            else:
                # アクセスに失敗した場合はリトライ回数を増やして再度試行
                retry_count += 1
                continue
        except requests.RequestException as e:
            # アクセス中に例外が発生した場合、エラーメッセージをログに記録し、失敗を返す
            logging.error(f"Error occurred while accessing {url}: {str(e)}")
            return url, [], response.status_code

    else:
        # 最大リトライ回数に達した場合、失敗をログに記録し、失敗を返す
        logging.error(f"Failed to retrieve URL: {url}")
        return url, [], response.status_code

    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    
    # CSSセレクタの配列
    selectors = [
        ('body > div:nth-child(2) > div.org_wrapper.germany_wrapper > section.car__price-list > div.car__price-list__table', 'text')

    ]

    scraped_data = [[] for _ in range(len(selectors))]
    
    # 各セレクターに対してスクレイピングを実行し、結果を保存
    for index, (selector, *data_types) in enumerate(selectors):
        elements = soup.select(selector)
        if 'link' in data_types:
            # リンクのテキストとURLを抽出
            scraped_data[index] = [(element.get('href', ''), element.get_text(strip=True)) for element in elements]
        else:
            # テキストのみを抽出
            scraped_data[index] = [element.get_text(strip=True).encode('utf-8').decode('utf-8') for element in elements]
    
    time.sleep(delay_time)  # さらに遅延を挟む
    print(f'{delay_time}秒の遅延処理 / status code{response.status_code} {scraped_data}')
    return url, scraped_data, response.status_code



# スクレイピングの進捗をログに記録する関数
def log_progress(completed_count, total_count):
    percentage_complete = (completed_count / total_count) * 100
    print(f'{round(percentage_complete, 2)} % 完了.... {completed_count} / {total_count}')

# 完了したURLの数
completed_count = 0

# CSVファイルを開き、ヘッダーとスクレイプしたデータを書き込む
with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header_row)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # URLリストに対して並行してスクレイピングを実行
        for url in urls:
            result = scrape_url(url)  # 各URLに対してスクレイピングを実行
            url, scraped_data, status_code = result
            max_length = max(len(data) for data in scraped_data)  # 最大の列数を取得
            
            # スクレイプしたデータを行としてCSVに書き込む
            for i in range(max_length):
                row_data = [url] + [data[i] if i < len(data) else '' for data in scraped_data] + [status_code]
                csv_writer.writerow(row_data)

            completed_count += 1  # 完了したURLの数を更新
            log_progress(completed_count, len(urls))  # 進捗のログ

            print(f'{header_row[0]}: {url}')  # 完了したURLを表示
            print(' ')
            print('--------------------------------------------')

print('スクレイピングが完了しました。')  # 全てのスクレイピングが完了したことを通知
