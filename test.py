from setting_file.header import *

# ファイルパス
file_directory = file_path.file_directory # file_path.py で定義したファイルディレクトリを指定
file_name = "scraped_data.csv"
output_file = os.path.join(file_directory, file_name)


# GCPサービスアカウントの認証情報を設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = api_json.ocrapi

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

def detect_text_from_image(image_path):
    """画像ファイルからテキストを抽出する関数"""
    client = vision.ImageAnnotatorClient()
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts[0].description if texts else ''

def detect_text_from_pdf(pdf_path, bucket_name):
    """PDFファイルからテキストを抽出する関数"""
    client = vision.ImageAnnotatorClient()

    # PDFファイルをCloud Storageにアップロード
    destination_blob_name = os.path.basename(pdf_path)
    upload_blob(bucket_name, pdf_path, destination_blob_name)

    gcs_source_uri = f'gs://{bucket_name}/{destination_blob_name}'
    gcs_source = vision.GcsSource(uri=gcs_source_uri)
    input_config = vision.InputConfig(gcs_source=gcs_source, mime_type='application/pdf')

    features = [vision.Feature(type_=vision.Feature.Type.DOCUMENT_TEXT_DETECTION)]

    # アノテーションリクエスト
    request = vision.AnnotateFileRequest(features=features, input_config=input_config)

    # バッチアノテーションリクエスト
    response = client.batch_annotate_files(requests=[request])
    
    text = ""
    for page_response in response.responses[0].responses:
        text += page_response.full_text_annotation.text

    return text

def extract_text(file_path, bucket_name):
    """ファイルの種類を判別し、適切な方法でテキストを抽出する関数"""
    _, ext = os.path.splitext(file_path)
    if ext.lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']:
        return detect_text_from_image(file_path)
    elif ext.lower() == '.pdf':
        return detect_text_from_pdf(file_path, bucket_name)
    else:
        raise ValueError(f'Unsupported file type: {ext}')

def process_csv_files(csv_directory, input_csv_filenames, bucket_name):
    """CSVファイルを処理し、画像またはPDFファイルから抽出したテキストをテキストファイルに保存する関数"""
    for input_csv_filename in input_csv_filenames:
        input_file = os.path.join(csv_directory, input_csv_filename)
        output_text_filename = input_csv_filename.replace('.csv', '_整形後.txt')
        output_file = os.path.join(csv_directory, output_text_filename)
        
        # CSVファイルを読み込む
        df = pd.read_csv(input_file)
        
        # 抽出したテキストをテキストファイルに保存する
        with open(output_file, 'w', encoding='utf-8') as f:
            for file_path in df['file_path']:
                try:
                    text = extract_text(file_path, bucket_name)
                    f.write(f'File path: {file_path}\n')
                    f.write(f'Extracted text:\n{text}\n')
                    f.write('-' * 80 + '\n')
                except ValueError as e:
                    f.write(f'Error processing file {file_path}: {e}\n')
                    f.write('-' * 80 + '\n')
        
        print(f'Processed file saved as: {output_file}')

# ファイルパスの指定
csv_directory = 'path/to/csv_directory'  # 適切なディレクトリパスに置き換える
input_csv_filenames = [
    'garagecurrent.com.access_log_20240707.csv',
    # 他のCSVファイルも必要に応じて追加する
]
bucket_name = 'your-gcs-bucket-name'  # Cloud Storageバケット名を指定する

# CSVファイルを処理する
process_csv_files(csv_directory, input_csv_filenames, bucket_name)
