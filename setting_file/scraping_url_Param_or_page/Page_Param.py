class PageParamUrlGenerator:
    def __init__(self, base_url, parameter="", pagenation_min=1, pagenation_max=1):
        """
        コンストラクタでURL生成の設定を受け取る
        """
        self.base_url = base_url
        self.parameter = parameter
        self.pagenation_min = pagenation_min
        self.pagenation_max = pagenation_max

    def generate_urls(self):
        """
        ページネーションのURLリストを生成
        """
        return [
            self.base_url.format(i) + self.parameter
            for i in range(self.pagenation_min, self.pagenation_max + 1)
        ]
