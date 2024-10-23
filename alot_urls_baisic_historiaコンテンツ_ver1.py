from setting_file.header import *


# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定
file_name = "Qscraped_data.csv"
output_file = os.path.join(file_directory, file_name)

# # スプレッドシート認証
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# credentials = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/STAFF1088/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/python-scrape.json", scope)
# gc = gspread.authorize(credentials)
# ヘッダー行の設定。ここではウェブページからスクレイプする項目名を列挙しています


header_row = ['URL', 'メーカー', '車種タイトル', '車輌本体価格(basePrice__content)', '走行距離', '年式(specList__jpYear)', '修復歴']

urls = [
'https://www.qsha-oh.com/historia/article/repair-or-junk',
'https://www.qsha-oh.com/historia/article/toyota-crown',
'https://www.qsha-oh.com/historia/article/pepper-mill',
'https://www.qsha-oh.com/historia/article/beat',
'https://www.qsha-oh.com/historia/article/ending-note',
'https://www.qsha-oh.com/historia/article/snowy-roads-with-normal-tires',
'https://www.qsha-oh.com/historia/article/land_cruiser_60_malfunction',
'https://www.qsha-oh.com/historia/article/used-car-gasoline',
'https://www.qsha-oh.com/historia/article/scrapped-cars-and-dismantling-of-cars',
'https://www.qsha-oh.com/historia/article/rassemblement-mensuel-a-st-maur-des-fosses-france',
'https://www.qsha-oh.com/historia/article/night-drive',
'https://www.qsha-oh.com/historia/article/old-car-child-seat',
'https://www.qsha-oh.com/historia/article/light-vehicle-scrapping-cost',
'https://www.qsha-oh.com/historia/article/sunny-truck',
'https://www.qsha-oh.com/historia/article/car-breakdown',
'https://www.qsha-oh.com/historia/article/gogomtg-2023-vol1-porsche',
'https://www.qsha-oh.com/historia/article/yaho-2022',
'https://www.qsha-oh.com/historia/article/qsha-oh-cm1',
'https://www.qsha-oh.com/historia/article/vanagon-maintenance-costs',
'https://www.qsha-oh.com/historia/writer/atts',
'https://www.qsha-oh.com/historia/article/automobile-tax-and-junk-car',
'https://www.qsha-oh.com/historia/article/pollen-on-car',
'https://www.qsha-oh.com/historia/article/elizabeth-II-queen-of-the-united-kingdom-landrover',
'https://www.qsha-oh.com/historia/article/car-snow-accident',
'https://www.qsha-oh.com/historia/article/italian-driving-regulations-manners',
'https://www.qsha-oh.com/historia/article/subaru-360-restore',
'https://www.qsha-oh.com/historia/article/suzuki-cars-india',
'https://www.qsha-oh.com/historia/article/kato-kumiko',
'https://www.qsha-oh.com/historia/article/1990s-vol10-honda-ascot-rafaga',
'https://www.qsha-oh.com/historia/article/corolla-sprinter-driversmtg-2022',
'https://www.qsha-oh.com/historia/article/fj-cruiser-2',
'https://www.qsha-oh.com/historia/article/gogomtg-2023-vol2-unique-cars',
'https://www.qsha-oh.com/historia/article/daihatsu-leeza-hamachi',
'https://www.qsha-oh.com/historia/article/how-to-get-a-garage-certificate',
'https://www.qsha-oh.com/historia/article/mercedes-amg',
'https://www.qsha-oh.com/historia/article/r35-gt-r-fuel-efficiency',
'https://www.qsha-oh.com/historia/article/driving-broken-down-car',
'https://www.qsha-oh.com/historia/article/chaser',
'https://www.qsha-oh.com/historia/article/germany-mercedes-benz-240d-w123-wilhelm',
'https://www.qsha-oh.com/historia/article/prado_150-resale-value',
'https://www.qsha-oh.com/historia/article/fade-phenomenon',
'https://www.qsha-oh.com/historia/article/vehicle-inspection-expired-move',
'https://www.qsha-oh.com/historia/article/matsudo-vol7',
'https://www.qsha-oh.com/historia/article/restructuring',
'https://www.qsha-oh.com/historia/article/jimny-ja22',
'https://www.qsha-oh.com/historia/article/yan-maruuama-okayama-drift-driver',
'https://www.qsha-oh.com/historia/article/r35-gt-r-tire',
'https://www.qsha-oh.com/historia/article/about-classic-car',
'https://www.qsha-oh.com/historia/article/taiwan-asian-three-box-sedan-classics',
'https://www.qsha-oh.com/historia/article/prince-skyline-2000gt',
'https://www.qsha-oh.com/historia/article/hiace-failure',
'https://www.qsha-oh.com/historia/article/fairladyz-version-nismo',
'https://www.qsha-oh.com/historia/article/pioneer-vol2-subaru-regacy-touring-wagon',
'https://www.qsha-oh.com/historia/article/car-navigation',
'https://www.qsha-oh.com/historia/article/parking-manners-regulations-germany',
'https://www.qsha-oh.com/historia/article/land_cruiser_prado_95',
'https://www.qsha-oh.com/historia/article/vehicle-inspection-address-change-dealer-fees',
'https://www.qsha-oh.com/historia/article/car-inheritance-will',
'https://www.qsha-oh.com/historia/article/car-depreciation',
'https://www.qsha-oh.com/historia/article/alfa-spider-916-maintenance-costs',
'https://www.qsha-oh.com/historia/article/old-car-air-conditioner',
'https://www.qsha-oh.com/historia/article/fascinating-facts-about-carburetors-vol2',
'https://www.qsha-oh.com/historia/article/devils-whisper',
'https://www.qsha-oh.com/historia/article/monocoque-cafebar',
'https://www.qsha-oh.com/historia/article/paris-halloween-mgb',
'https://www.qsha-oh.com/historia/article/buying-a-used-foreign-car',
'https://www.qsha-oh.com/historia/article/submerged-car',
'https://www.qsha-oh.com/historia/article/car-repair-time',
'https://www.qsha-oh.com/historia/article/u-550-mtg-11th',
'https://www.qsha-oh.com/historia/article/car-undercover-repair-cost',
'https://www.qsha-oh.com/historia/article/honda-t360-part1',
'https://www.qsha-oh.com/historia/article/Initial-d',
'https://www.qsha-oh.com/historia/article/civic-type-r-ep3',
'https://www.qsha-oh.com/historia/article/omura-hideki',
'https://www.qsha-oh.com/historia/article/nissan-cube-3rd-generation',
'https://www.qsha-oh.com/historia/article/tire-puncture-repair',
'https://www.qsha-oh.com/historia/article/late-payment-on-car-loan',
'https://www.qsha-oh.com/historia/article/car-paint-peeling-repair',
'https://www.qsha-oh.com/historia/article/vol4',
'https://www.qsha-oh.com/historia/article/silvia-s14',
'https://www.qsha-oh.com/historia/article/lamborghini-maintenance-costs',
'https://www.qsha-oh.com/historia/article/vol2',
'https://www.qsha-oh.com/historia/article/mr-s-engine-swap',
'https://www.qsha-oh.com/historia/article/fairlady_z',
'https://www.qsha-oh.com/historia/article/seibu-keisatsu',
'https://www.qsha-oh.com/historia/article/land-cruiser-prado',
'https://www.qsha-oh.com/historia/article/sema-2022',
'https://www.qsha-oh.com/historia/article/student-car-loan',
'https://www.qsha-oh.com/historia/article/tele-hodai',
'https://www.qsha-oh.com/historia/article/no-will-inheritance-car',
'https://www.qsha-oh.com/historia/article/mazda-roadster',
'https://www.qsha-oh.com/historia/article/mr',
'https://www.qsha-oh.com/historia/article/be-prepared',
'https://www.qsha-oh.com/historia/article/chevrolet-impala',
'https://www.qsha-oh.com/historia/article/roadster',
'https://www.qsha-oh.com/historia/article/yurupean-meeting-14th',
'https://www.qsha-oh.com/historia/article/maserati-maintenance-costs',
'https://www.qsha-oh.com/historia/article/how-to-use-compound',
'https://www.qsha-oh.com/historia/article/sales-jobs',
'https://www.qsha-oh.com/historia/article/land_cruiser_80',
'https://www.qsha-oh.com/historia/article/automobile-tax-installments',
'https://www.qsha-oh.com/historia/article/matsudo-vol11',
'https://www.qsha-oh.com/historia/article/bongo-friendee-maintenance-costs',
'https://www.qsha-oh.com/historia/article/vehicle-inspection-address-change-online',
'https://www.qsha-oh.com/historia/article/180sx-price-increase',
'https://www.qsha-oh.com/historia/article/lexus-lfa-germany',
'https://www.qsha-oh.com/historia/article/cold-region-specification-vehicle',
'https://www.qsha-oh.com/historia/article/forester-sg9-sti-maintenance-costs',
'https://www.qsha-oh.com/historia/article/civic-country',
'https://www.qsha-oh.com/historia/article/1990s-vol8-suzuki-escudo',
'https://www.qsha-oh.com/historia/article/italy-la-festa-mille-miglia-2023-history',
'https://www.qsha-oh.com/historia/article/celsior-20',
'https://www.qsha-oh.com/historia/article/grassy-hero',
'https://www.qsha-oh.com/historia/article/broken-down-car-insurance',
'https://www.qsha-oh.com/historia/article/tips-for-track-meet-circuit-experience',
'https://www.qsha-oh.com/historia/article/cocoro-copen-2022',
'https://www.qsha-oh.com/historia/article/nissan-gtr-r35-eu-discontinued',
'https://www.qsha-oh.com/historia/article/summer-measures-for-old-cars',
'https://www.qsha-oh.com/historia/article/garage-certificate-sticker',
'https://www.qsha-oh.com/historia/article/germany-mt-44per',
'https://www.qsha-oh.com/historia/article/harrier-failure-point',
'https://www.qsha-oh.com/historia/article/nissan-ad-van-jun',
'https://www.qsha-oh.com/historia/article/what-is-scrap-car',
'https://www.qsha-oh.com/historia/article/sunny-b310-coupe',
'https://www.qsha-oh.com/historia/article/kubelwagen',
'https://www.qsha-oh.com/historia/article/kei-car-inheritance',
'https://www.qsha-oh.com/historia/article/ai-drawing-classic-cars-dall-e-img2img',
'https://www.qsha-oh.com/historia/article/automobile-tax-unexpired-amount',
'https://www.qsha-oh.com/historia/article/inheritance-car-automobile-tax',
'https://www.qsha-oh.com/historia/article/00-kei-vol2',
'https://www.qsha-oh.com/historia/article/kenmeri-gtr',
'https://www.qsha-oh.com/historia/article/grb-gvb-impreza-wrx-sti',
'https://www.qsha-oh.com/historia/article/cost-of-name-change',
'https://www.qsha-oh.com/historia/article/license-return-application-photo',
'https://www.qsha-oh.com/historia/article/t-bar-roof',
'https://www.qsha-oh.com/historia/article/neoclassic-px10',
'https://www.qsha-oh.com/historia/article/maintenance-cost-of-old-car',
'https://www.qsha-oh.com/historia/article/garage-certificate-moving',
'https://www.qsha-oh.com/historia/article/volvo-p1800-history',
'https://www.qsha-oh.com/historia/article/delica-d5-maintenance-costs',
'https://www.qsha-oh.com/historia/article/vol7-suzuki-wagonr-wide',
'https://www.qsha-oh.com/historia/article/aging-car',
'https://www.qsha-oh.com/historia/article/ibaraki-showa-no-kuruma-2023',
'https://www.qsha-oh.com/historia/article/prius-alpha',
'https://www.qsha-oh.com/historia/article/karmann-ghia',
'https://www.qsha-oh.com/historia/article/rx-7-fc3s-maintenance-costs',
'https://www.qsha-oh.com/historia/article/benz-190sl',
'https://www.qsha-oh.com/historia/article/leopard',
'https://www.qsha-oh.com/historia/article/name-change-letter-of-attorney',
'https://www.qsha-oh.com/historia/article/nissan-bluebird-hirakue',
'https://www.qsha-oh.com/historia/article/hiluxsurf-185',
'https://www.qsha-oh.com/historia/article/all_painting_car',
'https://www.qsha-oh.com/historia/article/copen-l880k',
'https://www.qsha-oh.com/historia/article/skyline-kenmeri',
'https://www.qsha-oh.com/historia/article/bmw-e30',
'https://www.qsha-oh.com/historia/article/compulsory-automobile-liability-insurance-2',
'https://www.qsha-oh.com/historia/article/flywheel',
'https://www.qsha-oh.com/historia/article/honda-t360-part2',
'https://www.qsha-oh.com/historia/article/crown-athlete',
'https://www.qsha-oh.com/historia/article/zero-1',
'https://www.qsha-oh.com/historia/article/garage-certificate-procedure',
'https://www.qsha-oh.com/historia/article/hilux-maintenance-costs',
'https://www.qsha-oh.com/historia/article/pajero-maintenance',
'https://www.qsha-oh.com/historia/article/2door-sedan',
'https://www.qsha-oh.com/historia/article/nissan-pao',
'https://www.qsha-oh.com/historia/article/land-rover-defender-90',
'https://www.qsha-oh.com/historia/article/who-pays-car-tax-after-sale',
'https://www.qsha-oh.com/historia/article/toyota-2000gt',
'https://www.qsha-oh.com/historia/article/r33-skyline-maintenance-costs',
'https://www.qsha-oh.com/historia/article/land_cruiser_60',
'https://www.qsha-oh.com/historia/article/starlet-ep82',
'https://www.qsha-oh.com/historia/article/automobile-tax-on-a-trade-in-car',
'https://www.qsha-oh.com/historia/article/leaf-spring',
'https://www.qsha-oh.com/historia/article/S2000-ap1',
'https://www.qsha-oh.com/historia/article/soarer-20',
'https://www.qsha-oh.com/historia/article/celsior-30-maintenance-costs',
'https://www.qsha-oh.com/historia/article/cedric-y31',
'https://www.qsha-oh.com/historia/article/car-insurance-for-loaner-car',
'https://www.qsha-oh.com/historia/article/germany-select-jp-sports',
'https://www.qsha-oh.com/historia/article/8-number-vehicle-inspection',
'https://www.qsha-oh.com/historia/article/headlights',
'https://www.qsha-oh.com/historia/article/lost-driving-license',
'https://www.qsha-oh.com/historia/article/car-scratch-touch-pen',
'https://www.qsha-oh.com/historia/article/car-squealing-sound',
'https://www.qsha-oh.com/historia/article/Returning-young-person-license',
'https://www.qsha-oh.com/historia/article/garage-certificate-2nd-car',
'https://www.qsha-oh.com/historia/article/parking-space-certification',
'https://www.qsha-oh.com/historia/article/land_cruiser_100',
'https://www.qsha-oh.com/historia/article/car-mileage',
'https://www.qsha-oh.com/historia/article/overhaul-engine',
'https://www.qsha-oh.com/historia/article/left-hand-drive',
'https://www.qsha-oh.com/historia/article/r30-skyline-2',
'https://www.qsha-oh.com/historia/article/toyota-carina-tetsugt',
'https://www.qsha-oh.com/historia/article/toyota-te27-charm',
'https://www.qsha-oh.com/historia/article/toyota-1jz-engine',
'https://www.qsha-oh.com/historia/article/mini-cooper-history',
'https://www.qsha-oh.com/historia/article/jimny-ja11-ja12-ja22',
'https://www.qsha-oh.com/historia/article/tyrell-p34-vol1',
'https://www.qsha-oh.com/historia/article/compulsory-automobile-liability-insurance',
'https://www.qsha-oh.com/historia/article/cresta-resale-value',
'https://www.qsha-oh.com/historia/article/bnr34skyline-gtr',
'https://www.qsha-oh.com/historia/article/cedric-330-series',
'https://www.qsha-oh.com/historia/article/pioneer-vol3-honda-fit',
'https://www.qsha-oh.com/historia/article/garage-certificate-rental-property',
'https://www.qsha-oh.com/historia/article/with-vehicle-inspection-maintenance',
'https://www.qsha-oh.com/historia/article/land_cruiser_prado_120',
'https://www.qsha-oh.com/historia/article/chaser-jzx100',
'https://www.qsha-oh.com/historia/article/car-loan-lump-sum-payment',
'https://www.qsha-oh.com/historia/article/car-slip',
'https://www.qsha-oh.com/historia/article/mazda-porter-van-kotani',
'https://www.qsha-oh.com/historia/article/lancer-evolution-wagon',
'https://www.qsha-oh.com/historia/article/car-covered-in-snow',
'https://www.qsha-oh.com/historia/article/25-year-rule-skyline-r34-gt-r',
'https://www.qsha-oh.com/historia/article/garage-certificate-required-documents-corporation',
'https://www.qsha-oh.com/historia/article/dodge-challenger-se',
'https://www.qsha-oh.com/historia/article/in-line-3-cylinder',
'https://www.qsha-oh.com/historia/article/s15-wifes-feelings',
'https://www.qsha-oh.com/historia/article/landcruiser-70-maintenance-costs',
'https://www.qsha-oh.com/historia/article/leaded-gasoline-car',
'https://www.qsha-oh.com/historia/article/wrx-sti',
'https://www.qsha-oh.com/historia/article/right-handle-germany',
'https://www.qsha-oh.com/historia/article/car-mirror-repair',
'https://www.qsha-oh.com/historia/article/date-of-first-registration',
'https://www.qsha-oh.com/historia/article/crown-royal-saloon-g',
'https://www.qsha-oh.com/historia/article/rx7-fd3s',
'https://www.qsha-oh.com/historia/article/honda-accord-euro-r',
'https://www.qsha-oh.com/historia/article/te37',
'https://www.qsha-oh.com/historia/article/change-the-name-of-car',
'https://www.qsha-oh.com/historia/article/rx-7-rotary-engine',
'https://www.qsha-oh.com/historia/article/repair-before-recall',
'https://www.qsha-oh.com/historia/article/what-is-driving-history-certificate',
'https://www.qsha-oh.com/historia/article/blue-bird-910',
'https://www.qsha-oh.com/historia/article/monthly-installment-of-automobile-tax',
'https://www.qsha-oh.com/historia/article/re-acquired-after-returning-license',
'https://www.qsha-oh.com/historia/article/old-cars-in-garages',
'https://www.qsha-oh.com/historia/article/proxy-application-for-license-return',
'https://www.qsha-oh.com/historia/article/mark-II-gx71',
'https://www.qsha-oh.com/historia/article/old-car-sinkitoroku',
'https://www.qsha-oh.com/historia/article/nissan-fairlady-z-S30',
'https://www.qsha-oh.com/historia/article/garage-certificate-acquisition-requirements',
'https://www.qsha-oh.com/historia/article/fr-sports-car',
'https://www.qsha-oh.com/historia/article/license-return-taxi-benefits',
'https://www.qsha-oh.com/historia/article/alivehoon',
'https://www.qsha-oh.com/historia/article/cruise-control',
'https://www.qsha-oh.com/historia/article/garage-certificate-light-vehicle',
'https://www.qsha-oh.com/historia/article/rover-mini',
'https://www.qsha-oh.com/historia/article/land_cruiser_200_2',
'https://www.qsha-oh.com/historia/article/at-mt',
'https://www.qsha-oh.com/historia/article/road-sign',
'https://www.qsha-oh.com/historia/article/car-rust-repair',
'https://www.qsha-oh.com/historia/article/car-oil-leak-repair',
'https://www.qsha-oh.com/historia/article/car-repair-loaner-car',
'https://www.qsha-oh.com/historia/article/old-car-battery-rise-cause',
'https://www.qsha-oh.com/historia/article/toyota-soara',
'https://www.qsha-oh.com/historia/article/car-license-plate-change',
'https://www.qsha-oh.com/historia/article/car-loan-name-change',
'https://www.qsha-oh.com/historia/article/garage-certificate-procedure2',
'https://www.qsha-oh.com/historia/article/brz-zc6-maintenance-costs',
'https://www.qsha-oh.com/historia/article/hybrid-car-winter-fuel-efficiency',
'https://www.qsha-oh.com/historia/article/hiace',
'https://www.qsha-oh.com/historia/article/lancer-evolution-9-maintenance-costs',
'https://www.qsha-oh.com/historia/article/supercharger',
'https://www.qsha-oh.com/historia/article/porsche996-997',
'https://www.qsha-oh.com/historia/article/fuel-consumption-of-the-old-fit',
'https://www.qsha-oh.com/historia/article/vol5',
'https://www.qsha-oh.com/historia/article/impreza-wrx-sti-grb-maintenance-costs',
'https://www.qsha-oh.com/historia/article/hakosuka',
'https://www.qsha-oh.com/historia/article/drift-car',
'https://www.qsha-oh.com/historia/article/datsun-pickup-maintenance-costs',
'https://www.qsha-oh.com/historia/article/fairladyz-s30-maintenance-costs',
'https://www.qsha-oh.com/historia/article/toyota-porte',
'https://www.qsha-oh.com/historia/article/change-car-color',
'https://www.qsha-oh.com/historia/article/daihatsu-tanto-2th',
'https://www.qsha-oh.com/historia/article/how-to-repair-stucked-screws',
'https://www.qsha-oh.com/historia/article/horizontally-opposed-engine-merit-demerit',
'https://www.qsha-oh.com/historia/article/old-car-bubble-burst',
'https://www.qsha-oh.com/historia/article/nostalgic-2days-2024-report',
'https://www.qsha-oh.com/historia/article/car-transfer-certificate',
'https://www.qsha-oh.com/historia/article/lexus-ls-maintenance-costs',
'https://www.qsha-oh.com/historia/article/name-change-cost',
'https://www.qsha-oh.com/historia/article/how-to-use-engine-brake',
'https://www.qsha-oh.com/historia/article/harrier-30',
'https://www.qsha-oh.com/historia/article/4-number-vehicle-inspection',
'https://www.qsha-oh.com/historia/article/carburetor-car-maintenance',
'https://www.qsha-oh.com/historia/article/lexus-maintenance-costs',
'https://www.qsha-oh.com/historia/article/stagea',
'https://www.qsha-oh.com/historia/article/2cv-citroen-france',
'https://www.qsha-oh.com/historia/article/lancer-1600sgr',
'https://www.qsha-oh.com/historia/article/2-stroke-engine',
'https://www.qsha-oh.com/historia/article/civic-typer-ek9',
'https://www.qsha-oh.com/historia/article/x-trail-t31-type-maintenance-costs',
'https://www.qsha-oh.com/historia/article/drivers-epileptic-seizures',
'https://www.qsha-oh.com/historia/article/ferrari_512tr',
'https://www.qsha-oh.com/historia/article/old-car-racer',
'https://www.qsha-oh.com/historia/article/time-to-buy-a-car',
'https://www.qsha-oh.com/historia/article/discontinued-sports-car',
'https://www.qsha-oh.com/historia/article/car-repair-loan',
'https://www.qsha-oh.com/historia/article/30soarer-resale-value',
'https://www.qsha-oh.com/historia/article/hummer',
'https://www.qsha-oh.com/historia/article/vehicle-inspection-address-change-2-or-more-times',
'https://www.qsha-oh.com/historia/article/car-repair-estimate-only',
'https://www.qsha-oh.com/historia/article/vehicle-inspection-certificate-address-change',
'https://www.qsha-oh.com/historia/article/remaining-credit-re-loan',
'https://www.qsha-oh.com/historia/article/skyline-gt-r-specification',
'https://www.qsha-oh.com/historia/article/ichijimassyou-old-car-tax',
'https://www.qsha-oh.com/historia/article/mercedes-benz-190e-2-5-evo2',
'https://www.qsha-oh.com/historia/article/ford-gtd40',
'https://www.qsha-oh.com/historia/article/name-change-land-transport-office',
'https://www.qsha-oh.com/historia/article/mazda-mx-81',
'https://www.qsha-oh.com/historia/article/mot-test-certificate-dont-change-address-sell-car',
'https://www.qsha-oh.com/historia/article/sales-contract',
'https://www.qsha-oh.com/historia/article/25-year-rule-s2000',
'https://www.qsha-oh.com/historia/article/na-roadster-maintenance-costs',
'https://www.qsha-oh.com/historia/article/toyota-harrier-suv-pioneer-01',
'https://www.qsha-oh.com/historia/article/car-lease-inheritance',
'https://www.qsha-oh.com/historia/article/st185-celica-gt-four-tein-fujimoto-yoshirou',
'https://www.qsha-oh.com/historia/article/moderate-looseness',
'https://www.qsha-oh.com/historia/article/r32-skyline',
'https://www.qsha-oh.com/historia/article/taxi_movie',
'https://www.qsha-oh.com/historia/article/accident-car-tow',
'https://www.qsha-oh.com/historia/article/car-air-conditioner-repair',
'https://www.qsha-oh.com/historia/article/r35-gt-r-grade-difference',
'https://www.qsha-oh.com/historia/article/toyota-z30-soarer-3.0gtg-z30-jzz31',
'https://www.qsha-oh.com/historia/article/r34-skyline-gtr',
'https://www.qsha-oh.com/historia/article/car-gift-tax',
'https://www.qsha-oh.com/historia/article/fairlady_z_34',
'https://www.qsha-oh.com/historia/article/land-cruiser-70-troop-carrier',
'https://www.qsha-oh.com/historia/article/sunshade',
'https://www.qsha-oh.com/historia/article/gx71-mark2-resale-value',
'https://www.qsha-oh.com/historia/article/thermostat-replacement',
'https://www.qsha-oh.com/historia/article/land_cruiser_prado_78',
'https://www.qsha-oh.com/historia/article/engine-oil',
'https://www.qsha-oh.com/historia/article/land-cruiser-cygnus',
'https://www.qsha-oh.com/historia/article/old-car-restoration-cost',
'https://www.qsha-oh.com/historia/article/25-year-rule-lancerevolution-4/',
'https://www.qsha-oh.com/historia/article/25-year-rule-lancerevolution-6',
'https://www.qsha-oh.com/historia/article/mercedes-benz-tateme',
'https://www.qsha-oh.com/historia/article/aristo-vertex-edition',
'https://www.qsha-oh.com/historia/article/how-to-remove-stucked-screws',
'https://www.qsha-oh.com/historia/article/skyline-kenmeri-2',
'https://www.qsha-oh.com/historia/article/car-hail-damage-insurance',
'https://www.qsha-oh.com/historia/article/car-hail-damage-measures',
'https://www.qsha-oh.com/historia/article/car-hail-damage-measures/',
'https://www.qsha-oh.com/historia/article/1990s-vol9-mitsubishi-rvr',
'https://www.qsha-oh.com/historia/article/mazda-savanna',
'https://www.qsha-oh.com/historia/article/silvia-s14-maintenance-costs',
'https://www.qsha-oh.com/historia/article/vol6',
'https://www.qsha-oh.com/historia/article/mt-driving-method',
'https://www.qsha-oh.com/historia/article/hiace-200',
'https://www.qsha-oh.com/historia/article/jk-wrangler-maintenance-costs',
'https://www.qsha-oh.com/historia/article/ae-86',
'https://www.qsha-oh.com/historia/article/sports-car-scrapped',
'https://www.qsha-oh.com/historia/article/automobile-tax-address-change',
'https://www.qsha-oh.com/historia/article/stabilizer',
'https://www.qsha-oh.com/historia/article/harrier-60-resale-value',
'https://www.qsha-oh.com/historia/article/lancer-evolution-third-generation',
'https://www.qsha-oh.com/historia/article/license-plate-personal-information',
'https://www.qsha-oh.com/historia/article/car-winter-fuel-efficiency',
'https://www.qsha-oh.com/historia/article/synthetic-fuel',
'https://www.qsha-oh.com/historia/article/car-snow-removal',
'https://www.qsha-oh.com/historia/article/okayama-shoka-university-highschool-2023',
'https://www.qsha-oh.com/historia/article/harrier-60',
'https://www.qsha-oh.com/historia/article/alfaromeo-v6-busso',
'https://www.qsha-oh.com/historia/article/tyrell-p34-vol2',
'https://www.qsha-oh.com/historia/article/vapor-lock-phenomenon',
'https://www.qsha-oh.com/historia/article/personal-doctor',
'https://www.qsha-oh.com/historia/article/r35-gt-r-maintenance-cost',
'https://www.qsha-oh.com/historia/article/and_cruiser_80_malfunction',
'https://www.qsha-oh.com/historia/article/garage-certificate-cost',
'https://www.qsha-oh.com/historia/article/nissan-fairlady-z-S30-vol3',
'https://www.qsha-oh.com/historia/article/minica-toppo',
'https://www.qsha-oh.com/historia/article/tuna',
'https://www.qsha-oh.com/historia/article/garage-certificate-period',
'https://www.qsha-oh.com/historia/article/storage-space-usage-consent-certificate',
'https://www.qsha-oh.com/historia/article/change-of-address-on-drivers-license',
'https://www.qsha-oh.com/historia/article/fairladyz-s130',
'https://www.qsha-oh.com/historia/article/25-year-rule-altezza',
'https://www.qsha-oh.com/historia/article/nissan-safari-y60',
'https://www.qsha-oh.com/historia/article/25-year-rule-lancerevolution-4',
'https://www.qsha-oh.com/historia/article/nsx-maintenance-costs',
'https://www.qsha-oh.com/historia/article/subarist',
'https://www.qsha-oh.com/historia/article/lamborghini-miura',
'https://www.qsha-oh.com/historia/article/car-joint-ownership-inheritance',
'https://www.qsha-oh.com/historia/article/car-storage-law',
'https://www.qsha-oh.com/historia/article/german-h-license-plate',
'https://www.qsha-oh.com/historia/article/the-charm-of-the-land_cruiser_80',
'https://www.qsha-oh.com/historia/article/laurel-c130',
'https://www.qsha-oh.com/historia/article/mt_car',
'https://www.qsha-oh.com/historia/article/driving-earphone-violation',
'https://www.qsha-oh.com/historia/article/25-year-rule-silvia-s15',
'https://www.qsha-oh.com/historia/article/anti-crosswind-measures-for-cars',
'https://www.qsha-oh.com/historia/article/gt-r-engine-vr38dett',
'https://www.qsha-oh.com/historia/article/snow-tires',
'https://www.qsha-oh.com/historia/article/nozuru-s2000',
'https://www.qsha-oh.com/historia/article/carburetor',
'https://www.qsha-oh.com/historia/article/legal-maintenance',
'https://www.qsha-oh.com/historia/article/jimny-malfunction',
'https://www.qsha-oh.com/historia/article/mazda-cosmo',
'https://www.qsha-oh.com/historia/article/r34-skyline-25gtv',
'https://www.qsha-oh.com/historia/article/sr20-engine',
'https://www.qsha-oh.com/historia/article/welcome-old-car-3',
'https://www.qsha-oh.com/historia/article/fender-mirror',
'https://www.qsha-oh.com/historia/article/car-in-parents-name',
'https://www.qsha-oh.com/historia/article/matsudo-vol6',
'https://www.qsha-oh.com/historia/article/7-pitiful-japanese-cars-born-too-early',
'https://www.qsha-oh.com/historia/article/used-car-down-payment',
'https://www.qsha-oh.com/historia/article/matsumura-toru',
'https://www.qsha-oh.com/historia/article/accident-car-trade-in',
'https://www.qsha-oh.com/historia/article/car-purchase-flow',
'https://www.qsha-oh.com/historia/article/alfaromeo-146-naoki',
'https://www.qsha-oh.com/historia/writer/hayashi-tetsuya',
'https://www.qsha-oh.com/historia/article/stylish-classic-cars-berlin',
'https://www.qsha-oh.com/historia/article/recommended-touring-root-for-old-cars',
'https://www.qsha-oh.com/historia/article/shimada-kazuya',
'https://www.qsha-oh.com/historia/article/comparing-baseballteam-to-japanese-modern-classics',
'https://www.qsha-oh.com/historia/writer/toru-matsumura',
'https://www.qsha-oh.com/historia/writer/shouta-ogou',
'https://www.qsha-oh.com/historia/article/matsudo-bangai-1',
'https://www.qsha-oh.com/historia/category/germany-report',
'https://www.qsha-oh.com/historia/article/second-opinion',
'https://www.qsha-oh.com/historia/article/corolla-resale-value',
'https://www.qsha-oh.com/historia/article/used-car-license-plate-replacement',
'https://www.qsha-oh.com/historia/article/unused-new-car',
'https://www.qsha-oh.com/historia/article/the-christmas-carols',
'https://www.qsha-oh.com/historia/article/osugi',
'https://www.qsha-oh.com/historia/article/vehicle-inspection-3-years',
'https://www.qsha-oh.com/historia/article/skyline',
'https://www.qsha-oh.com/historia/article/celsior',
'https://www.qsha-oh.com/historia/article/s15-silvia-car-airconditioning-systems',
'https://www.qsha-oh.com/historia/writer/ou-ayato',
'https://www.qsha-oh.com/historia/article/how-to-buy-a-used-car',
'https://www.qsha-oh.com/historia/article/matsudo-vol8',
'https://www.qsha-oh.com/historia/article/dating-car-911',
'https://www.qsha-oh.com/historia/category/tyrellp34'
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
        ('#app > section > div.p-article__inner > div.p-article__content', 'text')

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
