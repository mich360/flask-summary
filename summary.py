
from janome.tokenizer import Tokenizer as JanomeTokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.tokenizers import Tokenizer

# 日本語の文章
text = """
赤沢亮正経済財政・再生相は23日、トランプ氏の発信内容については把握しているとしつつ「米国政府による正式な発表を待ちたい」と話した。赤沢氏が同日出席した日米関税交渉の閣僚協議で、日鉄とUSスチールの件を話しあったかは「差し控える」と述べるにとどめた。
23日の米株式市場ではトランプ氏のSNS投稿を受け、USスチールの株価が急騰した。一時は54ドルと前日比で26%高になった。日鉄が2023年12月に発表した買収提案時の価格である1株あたり55ドルに接近した。23日終値は52ドルだった。
"""

# 文単位で分割（簡易的に "。" で区切る）
sentences = text.replace("。\n", "。").split("。")
preprocessed_text = "。\n".join([s.strip() for s in sentences if s.strip() != ""]) + "。"

# sumyでパースして要約
parser = PlaintextParser.from_string(preprocessed_text, Tokenizer("japanese"))
summarizer = LexRankSummarizer()
summary = summarizer(parser.document, 2)

# 出力
print("要約結果:")
for sentence in summary:
    print("-", sentence)
